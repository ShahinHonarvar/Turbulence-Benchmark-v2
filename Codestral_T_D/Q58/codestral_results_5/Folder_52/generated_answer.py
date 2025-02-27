import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 147
    rows, cols = matrix.shape
    count = 0
    for row_start in range(rows):
        for col_start in range(cols):
            for row_end in range(row_start, rows):
                for col_end in range(col_start, cols):
                    if np.sum(matrix[row_start:row_end + 1, col_start:col_end + 1]) == n:
                        count += 1
    return count