import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(len(matrix) - 2):
        for j in range(len(matrix[i]) - 2):
            for x in range(i + 3, len(matrix) + 1):
                for y in range(j + 3, len(matrix[i]) + 1):
                    sub = matrix[i:x, j:y]
                    if np.sum(sub) == -936:
                        submatrices.append(sub)
    return submatrices