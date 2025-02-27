import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    n = 166
    submatrices_count = 0
    for r_start in range(rows):
        for r_end in range(r_start, rows):
            for c_start in range(cols):
                for c_end in range(c_start, cols):
                    if (r_end - r_start + 1) * (c_end - c_start + 1) == n:
                        submatrices_count += 1
    return submatrices_count