import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    matrix_size = matrix.shape
    for row in range(matrix_size[0]):
        for col in range(matrix_size[1]):
            for row_end in range(row + 1, matrix_size[0] + 1):
                for col_end in range(col + 1, matrix_size[1] + 1):
                    submatrix = matrix[row:row_end, col:col_end]
                    if np.sum(submatrix) == -308:
                        result.append(submatrix)
    return result