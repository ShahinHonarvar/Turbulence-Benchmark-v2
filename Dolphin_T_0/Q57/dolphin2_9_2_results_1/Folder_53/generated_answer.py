import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == -37:
                submatrices.append([[-37]])
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    if np.sum(matrix[i:k + 1, j:l + 1]) == -37:
                        submatrices.append(matrix[i:k + 1, j:l + 1].tolist())
    return submatrices