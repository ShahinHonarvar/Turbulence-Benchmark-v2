import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    if rows < 4 or cols < 4:
        return 0

    def count_submatrices(n_rows, n_cols):
        return (rows - n_rows + 1) * (cols - n_cols + 1)
    return count_submatrices(4, 4)