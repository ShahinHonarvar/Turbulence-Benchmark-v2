import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 122
    matrix_height, matrix_width = matrix.shape
    submatrix_count = 0
    for i in range(matrix_height - n + 1):
        for j in range(matrix_width - n + 1):
            submatrix = matrix[i:i + n, j:j + n]
            if np.isin(submatrix, [122]).sum() == n * n:
                submatrix_count += 1
    return submatrix_count