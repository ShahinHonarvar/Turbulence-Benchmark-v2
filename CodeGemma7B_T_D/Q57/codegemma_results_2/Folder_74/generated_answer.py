import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(matrix.shape[0]):
        for k in range(i + 1, matrix.shape[0] + 1):
            for j in range(matrix.shape[1]):
                for l in range(j + 1, matrix.shape[1] + 1):
                    sub_matrix = matrix[i:k, j:l]
                    sub_matrix_sum = sub_matrix.sum()
                    if sub_matrix_sum == 88:
                        result.append(sub_matrix)
    return result