import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    n = 90
    for row in range(rows):
        for col in range(cols):
            submatrix_rows = rows - row
            submatrix_cols = cols - col
            for sub_row in range(1, submatrix_rows + 1):
                for sub_col in range(1, submatrix_cols + 1):
                    if sub_row * sub_col == n:
                        submatrix = matrix[row:row + sub_row, col:col + sub_col]
                        if np.size(submatrix) == n:
                            count += 1
    return count