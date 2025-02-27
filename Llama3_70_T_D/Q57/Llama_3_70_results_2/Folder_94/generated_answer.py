import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    for row in range(rows):
        for col in range(cols):
            for sub_rows in range(row, rows):
                for sub_cols in range(col, cols):
                    sub_matrix = matrix[row:sub_rows + 1, col:sub_cols + 1]
                    if np.sum(sub_matrix) == 92:
                        result.append(sub_matrix.tolist())
    return result