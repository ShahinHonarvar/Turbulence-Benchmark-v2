import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    matrix_shape = matrix.shape
    n = 21
    for i in range(matrix_shape[0] - n + 1):
        for j in range(matrix_shape[1] - n + 1):
            submatrix = matrix[i:i + n, j:j + n]
            if np.linalg.matrix_rank(submatrix) == n:
                submatrix_count += 1
    return submatrix_count