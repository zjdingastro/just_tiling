

from just_tiling.hyperuniform.hyperuniform_tiling import hyperuniform_tiling

inputcatalog = "./lightcone_ra_0_90_dec_0_90_rmagcut20.5_cluster_mask.fits"
outputdir = "./" 

hyperuniform_tiling(inputcatalog, outputdir)
