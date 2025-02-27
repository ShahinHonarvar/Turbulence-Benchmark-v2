import numpy as np
from scipy.submatrix import submatrix_count

def submatrix_with_n_numbers(matrix):
    return submatrix_count(matrix, 83)