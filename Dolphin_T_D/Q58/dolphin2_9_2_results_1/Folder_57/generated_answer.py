import numpy as np

def submatrix_with_n_numbers(matrix):
    return np.sum(matrix.reshape(-1, matrix.shape[-1]) == 92).reshape(matrix.shape[:-1]).sum()