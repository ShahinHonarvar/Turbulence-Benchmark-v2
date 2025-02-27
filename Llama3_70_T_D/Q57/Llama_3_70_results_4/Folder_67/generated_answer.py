import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[1]):
            for sub_row in range(row, matrix.shape[0]):
                for sub_col in range(col, matrix.shape[1]):
                    submatrix = matrix[row:sub_row + 1, col:sub_col + 1]
                    if np.sum(submatrix) == 40:
                        result.append(submatrix.tolist())
    return result