import numpy as np

def submatrix_with_n_numbers(matrix, n=146):
    submatrix_count = 0
    matrix_rows = matrix.shape[0]
    matrix_cols = matrix.shape[1]
    for i in range(matrix_rows):
        for j in range(matrix_cols):
            for k in range(i + 1, matrix_rows + 1):
                for l in range(j + 1, matrix_cols + 1):
                    submatrix = matrix[i:k, j:l]
                    if len(submatrix.flatten()) == n:
                        submatrix_count += 1
    return submatrix_count