import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    for row_from in range(rows):
        for row_to in range(row_from, rows):
            for col_from in range(cols):
                for col_to in range(col_from, cols):
                    submatrix = matrix[row_from:row_to + 1, col_from:col_to + 1]
                    if np.sum(submatrix) == 40:
                        result.append(submatrix)
    return result