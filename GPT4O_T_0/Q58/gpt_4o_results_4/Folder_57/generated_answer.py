import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows):
        for c in range(cols):
            for sub_r in range(r, rows):
                for sub_c in range(c, cols):
                    if (sub_r - r + 1) * (sub_c - c + 1) == 92:
                        count += 1
    return count