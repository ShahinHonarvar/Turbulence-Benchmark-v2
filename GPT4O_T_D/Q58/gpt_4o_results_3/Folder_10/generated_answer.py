import numpy as np

def submatrix_with_n_numbers(matrix):
    total_submatrices = 0
    rows, cols = matrix.shape
    n = 56
    if rows * cols < n:
        return 0
    for r_start in range(rows):
        for c_start in range(cols):
            for r_end in range(r_start, rows):
                for c_end in range(c_start, cols):
                    row_count = r_end - r_start + 1
                    col_count = c_end - c_start + 1
                    if row_count * col_count == n:
                        total_submatrices += 1
    return total_submatrices