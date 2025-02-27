import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    n = 90
    total_submatrices = 0
    for i in range(row_count):
        for j in range(col_count):
            rows_remaining = row_count - i
            cols_remaining = col_count - j
            if rows_remaining * cols_remaining >= n:
                total_submatrices += 1
    return total_submatrices