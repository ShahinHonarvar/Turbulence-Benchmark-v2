import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    target_count = 42
    for row in range(rows):
        for col in range(cols):
            for sub_row in range(row + 1, rows + 1):
                for sub_col in range(col + 1, cols + 1):
                    sub_matrix = matrix[row:sub_row, col:sub_col]
                    if np.sum(sub_matrix) == target_count:
                        count += 1
    return count