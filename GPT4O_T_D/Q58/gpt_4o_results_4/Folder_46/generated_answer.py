import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    submatrix_count = 0
    for i in range(rows):
        for j in range(cols):
            for h in range(i + 1, rows + 1):
                for k in range(j + 1, cols + 1):
                    if (h - i) * (k - j) == 144:
                        submatrix_count += 1
    return submatrix_count