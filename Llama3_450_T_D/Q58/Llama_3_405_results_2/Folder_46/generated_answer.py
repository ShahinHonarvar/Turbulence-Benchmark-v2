import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n = 144
    rows, cols = matrix.shape
    for row in range(rows):
        for col in range(cols):
            for submatrix_rows in range(1, rows - row + 1):
                for submatrix_cols in range(1, cols - col + 1):
                    if submatrix_rows * submatrix_cols == n:
                        submatrix = matrix[row:row + submatrix_rows, col:col + submatrix_cols]
                        if submatrix.size == n:
                            count += 1
    return count