import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    if rows * cols < 7:
        return 0
    for r_start in range(rows):
        for r_end in range(r_start, rows):
            for c_start in range(cols):
                for c_end in range(c_start, cols):
                    submatrix_size = (r_end - r_start + 1) * (c_end - c_start + 1)
                    if submatrix_size == 7:
                        count += 1
    return count