import numpy as np

def submatrix_with_n_numbers(matrix):
    num_rows, num_cols = matrix.shape
    if num_rows < 40 or num_cols < 40:
        return 0
    submatrix_count = 0
    for row_start in range(num_rows - 39):
        for col_start in range(num_cols - 39):
            submatrix = matrix[row_start:row_start + 40, col_start:col_start + 40]
            if np.all(submatrix == 40):
                submatrix_count += 1
    return submatrix_count