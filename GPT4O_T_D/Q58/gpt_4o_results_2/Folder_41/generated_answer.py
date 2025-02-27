import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for r in range(rows):
        for c in range(cols):
            for sub_rows in range(1, rows - r + 1):
                for sub_cols in range(1, cols - c + 1):
                    if sub_rows * sub_cols == 73:
                        count += 1
    return count