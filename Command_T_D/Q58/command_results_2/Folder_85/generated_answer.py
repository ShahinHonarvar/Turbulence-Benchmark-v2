import numpy as np

def submatrix_with_n_numbers(mat):
    return np.sum(np.any(np.any(mat, 13), 13), axis=0)