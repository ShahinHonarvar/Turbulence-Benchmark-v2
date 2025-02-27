import numpy as np

def submatrix_with_n_numbers(matrix):
    row_count, col_count = matrix.shape
    if row_count < 3 or col_count < 3:
        return 0
    count = (row_count - 2) * (col_count - 2)
    return count