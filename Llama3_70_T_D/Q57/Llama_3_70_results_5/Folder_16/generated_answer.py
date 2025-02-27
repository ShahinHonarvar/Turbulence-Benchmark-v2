import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    for row in range(rows):
        for col in range(cols):
            for row_end in range(row, rows):
                for col_end in range(col, cols):
                    submatrix = matrix[row:row_end + 1, col:col_end + 1]
                    if np.sum(submatrix) == -157:
                        result.append(submatrix)
    return result