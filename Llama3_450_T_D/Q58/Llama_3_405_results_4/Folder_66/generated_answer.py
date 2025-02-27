import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    n = 42
    for row in range(rows):
        for col in range(cols):
            for submatrix_row in range(row + 1, rows + 1):
                for submatrix_col in range(col + 1, cols + 1):
                    submatrix = matrix[row:submatrix_row, col:submatrix_col]
                    if submatrix.size == n:
                        count += 1
    return count