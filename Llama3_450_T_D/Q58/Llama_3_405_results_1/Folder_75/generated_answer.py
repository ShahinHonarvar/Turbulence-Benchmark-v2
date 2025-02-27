import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    target_size = 80
    for row in range(rows):
        for col in range(cols):
            for sub_row in range(row, rows):
                sub_col = col + target_size // (sub_row - row + 1) - 1
                if sub_col < cols:
                    if (sub_row - row + 1) * (sub_col - col + 1) == target_size:
                        count += 1
                else:
                    break
    return count