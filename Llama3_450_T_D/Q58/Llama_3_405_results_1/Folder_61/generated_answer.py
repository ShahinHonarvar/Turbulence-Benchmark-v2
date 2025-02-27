import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for row in range(rows):
        for col in range(cols):
            for sub_row in range(row, min(row + 2, rows)):
                for sub_col in range(col, min(col + 2, cols)):
                    submatrix = matrix[row:sub_row + 1, col:sub_col + 1]
                    if np.size(submatrix) == 4:
                        count += 1
    return count