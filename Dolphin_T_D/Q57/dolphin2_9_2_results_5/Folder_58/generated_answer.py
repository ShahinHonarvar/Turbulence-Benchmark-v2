import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for rows in range(i + 1, len(matrix) + 1):
                for cols in range(j + 1, len(matrix[0]) + 1):
                    submatrix = matrix[i:rows, j:cols]
                    if np.sum(submatrix) == -137:
                        submatrices.append(submatrix.tolist())
    return submatrices