import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 51
    matrix = np.array(matrix)
    return np.sum(matrix.reshape(-1, matrix.shape[-1]) == n)