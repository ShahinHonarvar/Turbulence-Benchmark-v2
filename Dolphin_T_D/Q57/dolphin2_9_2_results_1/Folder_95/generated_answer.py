import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[0]) - 1):
            partial_sum = matrix[i][j] + matrix[i][j + 1] + matrix[i + 1][j] + matrix[i + 1][j + 1]
            if partial_sum == 19:
                submatrices.append(matrix[i:i + 2, j:j + 2])
    return submatrices