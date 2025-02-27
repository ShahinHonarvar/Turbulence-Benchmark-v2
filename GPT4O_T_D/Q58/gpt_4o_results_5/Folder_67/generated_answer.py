import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 43
    count = 0
    rows, cols = matrix.shape
    for r1 in range(rows):
        for r2 in range(r1, rows):
            for c1 in range(cols):
                for c2 in range(c1, cols):
                    if (r2 - r1 + 1) * (c2 - c1 + 1) == n:
                        count += 1
    return count