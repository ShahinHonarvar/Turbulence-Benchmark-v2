import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[1]):
            for row_end in range(row, matrix.shape[0]):
                for col_end in range(col, matrix.shape[1]):
                    submatrix = matrix[row:row_end + 1, col:col_end + 1]
                    if np.sum(submatrix) == -137:
                        result.append(submatrix)
    return result