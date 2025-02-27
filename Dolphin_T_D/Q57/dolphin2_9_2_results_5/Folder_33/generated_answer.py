import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    matrix_rows, matrix_cols = matrix.shape
    for i in range(matrix_rows):
        for j in range(matrix_cols):
            for k in range(i + 1, matrix_rows + 1):
                for l in range(j + 1, matrix_cols + 1):
                    submatrix = matrix[i:k, j:l]
                    if np.sum(submatrix) == -811:
                        result.append(submatrix)
    return result