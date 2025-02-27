import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    matrix_rows = matrix.shape[0]
    matrix_cols = matrix.shape[1]
    for i in range(matrix_rows - 3):
        for j in range(matrix_cols - 3):
            if np.prod(matrix[i:i + 4, j:j + 4]) == 76:
                submatrix_count += 1
    return submatrix_count