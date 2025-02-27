import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for r in range(i, rows):
                for c in range(j, cols):
                    submatrix_size = (r - i + 1) * (c - j + 1)
                    if submatrix_size == 90:
                        count += 1
                    if submatrix_size > 90:
                        break
    return count