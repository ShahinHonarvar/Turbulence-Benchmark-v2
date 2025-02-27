import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    for row in range(rows):
        for col in range(cols):
            for sub_rows in range(row + 1, rows + 1):
                for sub_cols in range(col + 1, cols + 1):
                    submatrix = matrix[row:sub_rows, col:sub_cols]
                    if np.sum(submatrix) == 34:
                        result.append(submatrix)
    return result