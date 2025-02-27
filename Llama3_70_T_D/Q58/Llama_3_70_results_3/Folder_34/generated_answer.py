import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for row in range(rows):
        for col in range(cols):
            submatrix = matrix[row:, col:]
            submatrix_rows, submatrix_cols = submatrix.shape
            for sub_row in range(submatrix_rows):
                for sub_col in range(submatrix_cols):
                    if submatrix_rows - sub_row <= 83 and submatrix_cols - sub_col <= 83:
                        count += 1
    return count