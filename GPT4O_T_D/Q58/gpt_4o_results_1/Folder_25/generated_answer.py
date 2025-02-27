import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    total_count = 0
    for r_start in range(rows):
        for r_end in range(r_start, rows):
            for c_start in range(cols):
                for c_end in range(c_start, cols):
                    sub_matrix_size = (r_end - r_start + 1) * (c_end - c_start + 1)
                    if sub_matrix_size == 66:
                        total_count += 1
    return total_count