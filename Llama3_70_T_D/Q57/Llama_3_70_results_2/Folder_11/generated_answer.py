import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    for row in range(rows):
        for col in range(cols):
            for sub_row in range(row, rows):
                for sub_col in range(col, cols):
                    sub_matrix = matrix[row:sub_row + 1, col:sub_col + 1]
                    if np.sum(sub_matrix) == 38:
                        result.append(sub_matrix)
    return result