import numpy as np

def submatrix_with_n_numbers(matrix):
    matrix_rows, matrix_cols = matrix.shape
    submatrix_count = 0
    for rows in range(matrix_rows - 9):
        for cols in range(matrix_cols - 20):
            submatrix = matrix[rows:rows + 10, cols:cols + 20]
            if len(np.unique(submatrix)) == 180:
                submatrix_count += 1
    return submatrix_count