import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for row in range(rows):
        for col in range(cols):
            for sub_rows in range(1, rows - row + 1):
                for sub_cols in range(1, cols - col + 1):
                    if sub_rows * sub_cols == 93:
                        count += 1
    return count