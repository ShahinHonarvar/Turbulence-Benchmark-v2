import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows):
        for c in range(cols):
            for submatrix_rows in range(1, rows - r + 1):
                for submatrix_cols in range(1, cols - c + 1):
                    if submatrix_rows * submatrix_cols == 37:
                        count += 1
    return count