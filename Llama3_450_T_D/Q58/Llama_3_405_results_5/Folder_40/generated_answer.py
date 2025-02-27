import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for row in range(rows):
        for col in range(cols):
            if matrix[row, col] == 1:
                for sub_row in range(row, rows):
                    for sub_col in range(col, cols):
                        submat = matrix[row:sub_row + 1, col:sub_col + 1]
                        if np.sum(submat) == 1:
                            count += 1
    return count