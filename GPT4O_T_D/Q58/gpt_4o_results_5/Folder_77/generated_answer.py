import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    total_submatrices = 0
    size = 179
    for r_start in range(rows):
        for c_start in range(cols):
            for r_end in range(r_start, rows):
                for c_end in range(c_start, cols):
                    if (r_end - r_start + 1) * (c_end - c_start + 1) == size:
                        total_submatrices += 1
    return total_submatrices