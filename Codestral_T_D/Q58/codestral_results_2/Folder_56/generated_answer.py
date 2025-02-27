import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 68
    rows, cols = matrix.shape
    count = 0
    for r in range(rows):
        for c in range(cols):
            for sub_rows in range(r, rows):
                for sub_cols in range(c, cols):
                    submatrix = matrix[r:sub_rows + 1, c:sub_cols + 1]
                    if submatrix.size == n:
                        count += 1
    return count