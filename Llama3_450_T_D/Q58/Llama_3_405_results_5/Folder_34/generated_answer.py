import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    target_count = 83
    count = 0
    for row in range(rows):
        for col in range(cols):
            for sub_rows in range(1, rows - row + 1):
                for sub_cols in range(1, cols - col + 1):
                    sub_matrix = matrix[row:row + sub_rows, col:col + sub_cols]
                    if sub_matrix.size == target_count:
                        count += 1
    return count