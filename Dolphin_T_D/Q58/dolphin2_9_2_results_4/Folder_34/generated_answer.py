import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 83
    matrix_shape = matrix.shape
    result = 0
    for i in range(matrix_shape[0] - n + 1):
        for j in range(matrix_shape[1] - n + 1):
            if np.sum(matrix[i:i + n, j:j + n]) == n * n:
                result += 1
    return result