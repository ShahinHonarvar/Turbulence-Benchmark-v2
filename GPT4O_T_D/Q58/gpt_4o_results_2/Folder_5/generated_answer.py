import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for h in range(i, rows):
                for k in range(j, cols):
                    if (h - i + 1) * (k - j + 1) == 63:
                        count += 1
    return count