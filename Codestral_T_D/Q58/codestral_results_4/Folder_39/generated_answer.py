import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows):
        for c in range(cols):
            for row_size in range(r, rows):
                for col_size in range(c, cols):
                    submatrix = matrix[r:row_size + 1, c:col_size + 1]
                    if submatrix.size == 59:
                        count += 1
    return count