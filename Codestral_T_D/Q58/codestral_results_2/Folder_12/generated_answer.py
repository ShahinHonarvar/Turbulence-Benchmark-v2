import numpy as np

def submatrix_with_n_numbers(matrix, n=46):
    count = 0
    rows, cols = matrix.shape
    for r in range(rows):
        for c in range(cols):
            for i in range(r, rows):
                for j in range(c, cols):
                    if (i - r + 1) * (j - c + 1) == n:
                        count += 1
    return count