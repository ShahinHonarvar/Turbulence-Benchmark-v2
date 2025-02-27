import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    for row in range(rows):
        for col in range(cols):
            for row_end in range(row + 1, rows + 1):
                for col_end in range(col + 1, cols + 1):
                    submatrix = matrix[row:row_end, col:col_end]
                    if np.sum(submatrix) == -27:
                        result.append(submatrix)
    return result