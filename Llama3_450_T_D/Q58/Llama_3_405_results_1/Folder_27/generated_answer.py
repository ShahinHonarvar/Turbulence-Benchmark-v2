import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    n = 77
    for row in range(rows):
        for col in range(cols):
            for sub_row in range(row + 1, rows + 1):
                for sub_col in range(col + 1, cols + 1):
                    if (sub_row - row) * (sub_col - col) == n:
                        count += 1
    return count