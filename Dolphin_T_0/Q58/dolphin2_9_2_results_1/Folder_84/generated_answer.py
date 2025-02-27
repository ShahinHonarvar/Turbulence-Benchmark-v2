import numpy as np

def submatrix_with_n_numbers(matrix):
    return np.sum([np.array_equal(matrix[i:i + 2, j:j + 5], np.full((2, 5), 127)).astype(int) for i in range(matrix.shape[0] - 1) for j in range(matrix.shape[1] - 4)])