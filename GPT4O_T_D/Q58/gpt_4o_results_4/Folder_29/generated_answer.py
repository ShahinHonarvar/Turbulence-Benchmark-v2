import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    submatrix_size = (k - i + 1) * (l - j + 1)
                    if submatrix_size == 19:
                        count += 1
    return count