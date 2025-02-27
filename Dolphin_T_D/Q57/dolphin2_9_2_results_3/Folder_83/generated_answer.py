import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(len(matrix[0])):
                if k + j <= len(matrix[0]) and k > 0 and (sum(matrix[i][j:j + k]) == -15):
                    submatrices.append(matrix[i][j:j + k])
    return submatrices