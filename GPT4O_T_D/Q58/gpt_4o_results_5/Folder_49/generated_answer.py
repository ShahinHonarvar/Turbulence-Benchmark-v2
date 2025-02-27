import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    submatrix_count = 0
    min_elements = 72
    for sub_rows in range(1, rows + 1):
        for sub_cols in range(1, cols + 1):
            if sub_rows * sub_cols == min_elements:
                for i in range(rows - sub_rows + 1):
                    for j in range(cols - sub_cols + 1):
                        submatrix_count += 1
    return submatrix_count