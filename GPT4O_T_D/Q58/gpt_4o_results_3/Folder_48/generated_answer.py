import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    target_count = 130
    count = 0
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            for row_start in range(rows - i + 1):
                for col_start in range(cols - j + 1):
                    submatrix = matrix[row_start:row_start + i, col_start:col_start + j]
                    if submatrix.size == target_count:
                        count += 1
    return count