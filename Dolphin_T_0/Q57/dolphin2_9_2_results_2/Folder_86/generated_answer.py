import numpy as np
from itertools import combinations

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for r in range(i + 1, len(matrix) + 1):
                for c in range(j + 1, len(matrix[0]) + 1):
                    submatrix_sum = np.sum(matrix[i:r, j:c])
                    if submatrix_sum == -394:
                        submatrices.append(matrix[i:r, j:c])
    return submatrices