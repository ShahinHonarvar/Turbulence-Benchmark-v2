import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    target_size = 66
    for row in range(rows):
        for col in range(cols):
            for sub_row_size in range(1, rows - row + 1):
                for sub_col_size in range(1, cols - col + 1):
                    if sub_row_size * sub_col_size == target_size:
                        count += 1
    return count