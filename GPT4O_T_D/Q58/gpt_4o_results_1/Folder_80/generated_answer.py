import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    submatrix_count = 0
    for i in range(rows):
        for j in range(cols):
            for sub_rows in range(1, rows - i + 1):
                for sub_cols in range(1, cols - j + 1):
                    if sub_rows * sub_cols == 180:
                        submatrix_count += 1
    return submatrix_count