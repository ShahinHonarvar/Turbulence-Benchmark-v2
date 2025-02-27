import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for n in range(i + 1, len(matrix) + 1):
                for m in range(j + 1, len(matrix[0]) + 1):
                    if np.sum(matrix[i:n, j:m]) == 69:
                        submatrices.append(matrix[i:n, j:m].tolist())
    return submatrices