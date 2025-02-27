import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for submatrix_rows in range(1, rows - i + 1):
                for submatrix_cols in range(1, cols - j + 1):
                    if submatrix_rows * submatrix_cols == 144:
                        count += 1
    return count