import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    matrix_rows, matrix_cols = matrix.shape
    for i in range(matrix_rows - 1):
        for j in range(matrix_cols - 1):
            submatrix = matrix[i:i + 2, j:j + 2]
            if submatrix.sum() == 54:
                submatrix_count += 1
    return submatrix_count