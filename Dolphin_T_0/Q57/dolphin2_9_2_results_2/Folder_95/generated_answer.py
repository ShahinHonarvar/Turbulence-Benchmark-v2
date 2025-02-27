import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for x in range(i + 1, len(matrix) + 1):
                for y in range(j + 1, len(matrix[0]) + 1):
                    if np.sum(matrix[i:x, j:y]) == 19:
                        submatrices.append(matrix[i:x, j:y])
    return submatrices