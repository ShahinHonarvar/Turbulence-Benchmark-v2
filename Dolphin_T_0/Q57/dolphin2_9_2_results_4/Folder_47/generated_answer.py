import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    matrix_rows, matrix_cols = matrix.shape
    for i in range(matrix_rows):
        for j in range(matrix_cols):
            for k in range(i, matrix_rows):
                for l in range(j, matrix_cols):
                    submatrix_sum = np.sum(matrix[i:k + 1, j:l + 1])
                    if submatrix_sum == 27:
                        submatrices.append(matrix[i:k + 1, j:l + 1])
    return submatrices