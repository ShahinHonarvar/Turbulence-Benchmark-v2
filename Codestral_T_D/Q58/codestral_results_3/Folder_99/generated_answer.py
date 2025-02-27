import numpy as np

def submatrix_with_n_numbers(matrix, n=146):
    rows, cols = matrix.shape
    total = 0
    for row_start in range(rows):
        for col_start in range(cols):
            for row_end in range(row_start + 1, rows + 1):
                for col_end in range(col_start + 1, cols + 1):
                    submatrix = matrix[row_start:row_end, col_start:col_end]
                    if submatrix.size == n:
                        total += 1
    return total