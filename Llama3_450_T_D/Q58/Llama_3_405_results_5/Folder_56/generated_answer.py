import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    target_count = 68
    valid_submatrices = 0
    for row_start in range(rows):
        for col_start in range(cols):
            for row_end in range(row_start + 1, rows + 1):
                for col_end in range(col_start + 1, cols + 1):
                    submatrix = matrix[row_start:row_end, col_start:col_end]
                    if np.size(submatrix) == target_count:
                        valid_submatrices += 1
    return valid_submatrices