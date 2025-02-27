import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    num_count = 122
    submatrices_count = 0
    for row in range(rows):
        for col in range(cols):
            for sub_rows in range(1, rows - row + 1):
                for sub_cols in range(1, cols - col + 1):
                    if sub_rows * sub_cols == num_count:
                        submatrices_count += 1
    return submatrices_count