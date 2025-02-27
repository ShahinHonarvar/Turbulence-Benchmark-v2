import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, columns = matrix.shape
    submatrix_count = 0
    target_count = 45
    for sub_rows in range(1, rows + 1):
        for sub_cols in range(1, columns + 1):
            if sub_rows * sub_cols == target_count:
                for i in range(rows - sub_rows + 1):
                    for j in range(columns - sub_cols + 1):
                        submatrix = matrix[i:i + sub_rows, j:j + sub_cols]
                        submatrix_count += 1
    return submatrix_count