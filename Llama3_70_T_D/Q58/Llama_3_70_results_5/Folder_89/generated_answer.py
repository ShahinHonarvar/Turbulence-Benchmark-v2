import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    n = 18
    count = 0
    for row in range(rows):
        for col in range(cols):
            for submatrix_rows in range(row + 1, rows + 1):
                for submatrix_cols in range(col + 1, cols + 1):
                    submatrix = matrix[row:submatrix_rows, col:submatrix_cols]
                    if submatrix.size == n:
                        count += 1
    return count