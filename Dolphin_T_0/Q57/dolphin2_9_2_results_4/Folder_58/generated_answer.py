import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    matrix_sum = np.sum(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i + 1, len(matrix) + 1):
                for l in range(j + 1, len(matrix[0]) + 1):
                    sub_matrix_sum = np.sum(matrix[i:k, j:l])
                    if sub_matrix_sum == -137:
                        submatrices.append(matrix[i:k, j:l])
    if not submatrices:
        return []
    return submatrices