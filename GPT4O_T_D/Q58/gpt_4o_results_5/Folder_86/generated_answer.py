import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    if 138 > rows * cols:
        return 0
    count = 0
    for r1 in range(rows):
        for c1 in range(cols):
            total = 0
            for r2 in range(r1, rows):
                for c2 in range(c1, cols):
                    total += 1
                    if total == 138:
                        count += 1
                    if total > 138:
                        break
    return count