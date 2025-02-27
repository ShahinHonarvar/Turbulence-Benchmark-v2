import numpy as np
import itertools

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i + 1, len(matrix) + 1):
                for l in range(j + 1, len(matrix[0]) + 1):
                    sub = [row[j:l] for row in matrix[i:k]]
                    if np.sum(sub) == -43:
                        submatrices.append(sub)
    return submatrices