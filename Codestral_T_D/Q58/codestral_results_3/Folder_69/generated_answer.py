import numpy as np

def submatrix_with_n_numbers(matrix, n=126):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows):
        for c in range(cols):
            for r_len in range(r, rows):
                for c_len in range(c, cols):
                    if (r_len - r + 1) * (c_len - c + 1) == n:
                        count += 1
    return count