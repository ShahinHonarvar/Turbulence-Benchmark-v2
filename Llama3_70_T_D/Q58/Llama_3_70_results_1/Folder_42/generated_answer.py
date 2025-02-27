import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    for row_start in range(rows):
        for row_end in range(row_start, rows):
            for col_start in range(cols):
                for col_end in range(col_start, cols):
                    submatrix = matrix[row_start:row_end + 1, col_start:col_end + 1]
                    if submatrix.size == 193:
                        count += 1
    return count