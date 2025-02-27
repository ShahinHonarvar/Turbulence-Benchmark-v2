import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    n = 64
    for row in range(rows):
        for col in range(cols):
            for submatrix_rows in range(1, rows - row + 1):
                for submatrix_cols in range(1, cols - col + 1):
                    if submatrix_rows * submatrix_cols == n:
                        count += 1
    return count