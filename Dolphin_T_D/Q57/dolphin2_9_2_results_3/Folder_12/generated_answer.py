import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for row in range(i + 1, len(matrix) + 1):
                for col in range(j + 1, len(matrix[0]) + 1):
                    submatrix = matrix[i:row, j:col]
                    if np.sum(submatrix) == -83:
                        submatrices.append(submatrix.tolist())
    return submatrices