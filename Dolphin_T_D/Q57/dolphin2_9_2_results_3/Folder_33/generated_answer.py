import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    matrix_rows = matrix.shape[0]
    matrix_cols = matrix.shape[1]
    for i in range(matrix_rows):
        for j in range(matrix_cols):
            for k in range(i + 1, matrix_rows + 1):
                for l in range(j + 1, matrix_cols + 1):
                    submatrix_sum = np.sum(matrix[i:k, j:l])
                    if submatrix_sum == -811:
                        submatrices.append(matrix[i:k, j:l])
    return submatrices