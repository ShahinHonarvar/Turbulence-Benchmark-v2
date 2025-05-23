import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    target_numbers = 107
    count = 0
    for sub_rows in range(1, rows + 1):
        for sub_cols in range(1, cols + 1):
            if sub_rows * sub_cols == target_numbers:
                for i in range(rows - sub_rows + 1):
                    for j in range(cols - sub_cols + 1):
                        count += 1
    return count