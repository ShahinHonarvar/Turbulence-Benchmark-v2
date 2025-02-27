import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    n = 66
    count = 0
    for r_start in range(rows):
        for r_end in range(r_start + 1, rows + 1):
            for c_start in range(cols):
                for c_end in range(c_start + 1, cols + 1):
                    submatrix_size = (r_end - r_start) * (c_end - c_start)
                    if submatrix_size == n:
                        count += 1
    return count