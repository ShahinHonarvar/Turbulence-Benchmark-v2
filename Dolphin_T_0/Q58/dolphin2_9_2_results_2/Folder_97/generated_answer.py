import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    matrix_rows, matrix_cols = matrix.shape
    for i in range(matrix_rows - 10):
        for j in range(matrix_cols - 10):
            sub_matrix = matrix[i:i + 12, j:j + 12]
            if np.count_nonzero(sub_matrix == 120) == 120:
                submatrix_count += 1
    return submatrix_count