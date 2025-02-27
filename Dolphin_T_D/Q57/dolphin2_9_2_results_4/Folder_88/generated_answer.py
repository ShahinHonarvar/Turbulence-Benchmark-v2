import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[0]) - 1):
            if matrix[i][j] == -64:
                submatrices.append([[matrix[i][j]]])
            for k in range(i + 1, len(matrix)):
                for l in range(j + 1, len(matrix[0])):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.sum() == -64:
                        submatrices.append(submatrix)
    return submatrices