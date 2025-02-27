import numpy as np

def submatrix_with_n_numbers(matrix):
    sub_matrix_count = 0
    matrix_rows, matrix_cols = matrix.shape
    for i in range(matrix_rows):
        for j in range(matrix_cols):
            for k in range(i, matrix_rows):
                for l in range(j, matrix_cols):
                    if np.sum(matrix[i:k + 1, j:l + 1]) == 59:
                        sub_matrix_count += 1
    return sub_matrix_count