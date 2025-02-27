import numpy as np

def submatrix_with_n_numbers(matrix):
    return np.count_nonzero((np.sum(matrix, axis=1) == 20) & (np.sum(matrix, axis=2) == 20) & (np.sum(matrix, axis=0) == 20) & (np.sum(matrix, axis=3) == 20))