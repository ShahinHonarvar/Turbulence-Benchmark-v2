import numpy as np

def submatrix_with_n_numbers(matrix):
    n_rows, n_cols = matrix.shape
    count = 0
    for row_start in range(n_rows - 7):
        for col_start in range(n_cols - 7):
            submatrix = matrix[row_start:row_start + 8, col_start:col_start + 8]
            if np.all(submatrix == 48):
                count += 1
    return count