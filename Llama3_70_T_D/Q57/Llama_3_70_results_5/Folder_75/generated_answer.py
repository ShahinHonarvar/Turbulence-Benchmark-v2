import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    for row in range(rows):
        for col in range(cols):
            for sub_rows in range(row + 1, rows + 1):
                for sub_cols in range(col + 1, cols + 1):
                    sub_matrix = matrix[row:sub_rows, col:sub_cols]
                    if np.sum(sub_matrix) == 16:
                        result.append(sub_matrix)
    return result