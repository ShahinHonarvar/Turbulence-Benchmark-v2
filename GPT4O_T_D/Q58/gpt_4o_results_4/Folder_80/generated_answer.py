import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    submatrix_count = 0
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    sub_rows = k - i + 1
                    sub_cols = l - j + 1
                    if sub_rows * sub_cols == 180:
                        submatrix_count += 1
    return submatrix_count