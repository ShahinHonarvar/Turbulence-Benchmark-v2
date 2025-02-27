import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[i]) - 1):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[i])):
                    submatrix = np.array(matrix[i:k + 1, j:l + 1])
                    if np.sum(submatrix) == -137:
                        submatrices.append(submatrix)
    return submatrices