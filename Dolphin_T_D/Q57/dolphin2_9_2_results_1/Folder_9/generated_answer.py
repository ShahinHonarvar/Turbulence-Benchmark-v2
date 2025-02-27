import numpy as np
from itertools import combinations

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for i in range(rows):
        for j in range(cols):
            for k in range(i + 1, rows + 1):
                for l in range(j + 1, cols + 1):
                    submatrix_sum = np.sum(matrix[i:k, j:l])
                    if submatrix_sum == -86:
                        submatrices.append(matrix[i:k, j:l])
    if not submatrices:
        return []
    else:
        return submatrices