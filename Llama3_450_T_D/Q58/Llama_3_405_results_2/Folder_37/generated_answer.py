import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    target_size = 64
    for row in range(rows):
        for col in range(cols):
            for submatrix_row_size in range(1, rows - row + 1):
                for submatrix_col_size in range(1, cols - col + 1):
                    if submatrix_row_size * submatrix_col_size == target_size:
                        submatrix = matrix[row:row + submatrix_row_size, col:col + submatrix_col_size]
                        if submatrix.size == target_size:
                            count += 1
    return count