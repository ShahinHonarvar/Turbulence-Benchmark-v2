import numpy as np

def submatrix_with_n_numbers(matrix):
    size = matrix.shape[0] * matrix.shape[1]
    return np.count_nonzero((matrix == 85).sum(axis=1).repeat(matrix.shape[0]).reshape(-1, matrix.shape[0]) == size)