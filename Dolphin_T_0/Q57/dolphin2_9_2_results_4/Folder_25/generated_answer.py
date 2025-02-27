import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for row_start in range(i, matrix.shape[0] + 1):
                for col_start in range(j, matrix.shape[1] + 1):
                    current_submatrix = matrix[i:row_start, j:col_start]
                    if np.sum(current_submatrix) == -20:
                        submatrices.append(current_submatrix)
    return submatrices