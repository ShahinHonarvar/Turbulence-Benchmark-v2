import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    matrix_shape = matrix.shape
    n = 63
    for i in range(matrix_shape[0] - n + 1):
        for j in range(matrix_shape[1] - n + 1):
            if matrix[i:i + n, j:j + n].size == n * n:
                count += 1
    return count