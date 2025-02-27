import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    n = 115
    count = 0
    for r1 in range(rows):
        for r2 in range(r1, rows):
            for c1 in range(cols):
                for c2 in range(c1, cols):
                    submatrix_size = (r2 - r1 + 1) * (c2 - c1 + 1)
                    if submatrix_size == n:
                        count += 1
    return count