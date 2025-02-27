import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    submatrices = []
    for i in range(m):
        for j in range(n):
            for x in range(i + 1, m + 1):
                for y in range(j + 1, n + 1):
                    if np.sum(matrix[i:x, j:y]) == 245:
                        submatrices.append(matrix[i:x, j:y])
    return submatrices