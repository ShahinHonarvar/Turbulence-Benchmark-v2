import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    target_sum = 173
    for row_start in range(rows):
        for col_start in range(cols):
            for row_end in range(row_start + 1, rows + 1):
                for col_end in range(col_start + 1, cols + 1):
                    submatrix = matrix[row_start:row_end, col_start:col_end]
                    if submatrix.size == target_sum:
                        count += 1
    return count