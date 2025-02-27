import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    n = 18
    matrix_height, matrix_width = matrix.shape
    for i in range(matrix_height - n + 1):
        for j in range(matrix_width - n + 1):
            submatrix = matrix[i:i + n, j:j + n]
            if np.count_nonzero(submatrix == 1) == n * n:
                submatrix_count += 1
    return submatrix_count