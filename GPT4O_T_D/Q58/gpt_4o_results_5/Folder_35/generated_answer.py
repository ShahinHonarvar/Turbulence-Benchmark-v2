import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    if rows * cols < 111:
        return 0
    for r in range(rows):
        for c in range(cols):
            for r1 in range(r, rows):
                for c1 in range(c, cols):
                    if (r1 - r + 1) * (c1 - c + 1) == 111:
                        count += 1
    return count