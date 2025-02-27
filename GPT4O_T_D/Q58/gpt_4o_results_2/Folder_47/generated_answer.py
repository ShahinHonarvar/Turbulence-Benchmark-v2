import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    if rows < 1 or cols < 1:
        return 0
    count = 0
    total_elements = 90
    for submatrix_rows in range(1, rows + 1):
        for submatrix_cols in range(1, cols + 1):
            if submatrix_rows * submatrix_cols == total_elements:
                possible_submatrices_rows = rows - submatrix_rows + 1
                possible_submatrices_cols = cols - submatrix_cols + 1
                count += possible_submatrices_rows * possible_submatrices_cols
    return count