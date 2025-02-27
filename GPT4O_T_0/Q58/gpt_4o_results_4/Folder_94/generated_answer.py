import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows):
        for c in range(cols):
            for sub_rows in range(1, rows - r + 1):
                for sub_cols in range(1, cols - c + 1):
                    if sub_rows * sub_cols == 93:
                        count += 1
    return count