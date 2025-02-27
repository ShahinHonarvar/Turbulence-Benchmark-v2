import numpy as np

def submatrix_with_n_numbers(matrix, n=28):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows):
        for c in range(cols):
            for nr in range(r, rows):
                for nc in range(c, cols):
                    if (nr - r + 1) * (nc - c + 1) == n:
                        count += 1
    return count