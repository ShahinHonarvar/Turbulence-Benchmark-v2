import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    n = 64
    for row in range(rows):
        for col in range(cols):
            for submatrix_row in range(1, rows - row + 1):
                for submatrix_col in range(1, cols - col + 1):
                    if submatrix_row * submatrix_col == n:
                        submatrix = matrix[row:row + submatrix_row, col:col + submatrix_col]
                        count += 1
    return count