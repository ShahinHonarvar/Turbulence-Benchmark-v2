import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[1]):
            for sub_row in range(row + 1, matrix.shape[0] + 1):
                for sub_col in range(col + 1, matrix.shape[1] + 1):
                    sub_matrix = matrix[row:sub_row, col:sub_col]
                    if np.sum(sub_matrix) == -27:
                        result.append(sub_matrix.tolist())
    return result