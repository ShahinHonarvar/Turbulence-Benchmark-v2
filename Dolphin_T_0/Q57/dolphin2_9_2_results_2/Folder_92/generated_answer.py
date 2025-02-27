import numpy as np

def submatrix_with_particular_sum(matrix):
    n = len(matrix)
    result = []
    for i in range(n):
        for j in range(1, len(matrix[0])):
            matrix[i][j] += matrix[i][j - 1]
    for i in range(n):
        for j in range(len(matrix[0])):
            for k in range(i, n):
                for l in range(j, len(matrix[0])):
                    submatrix_sum = matrix[k][l]
                    if j > 0:
                        submatrix_sum -= matrix[k][j - 1]
                    if i > 0:
                        submatrix_sum -= matrix[i - 1][l]
                    if i > 0 and j > 0:
                        submatrix_sum += matrix[i - 1][j - 1]
                    if submatrix_sum == -3:
                        result.append((i, j, k, l))
    return result