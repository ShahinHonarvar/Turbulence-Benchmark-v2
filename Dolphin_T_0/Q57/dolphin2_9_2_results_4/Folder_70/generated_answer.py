import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    submatrices = []
    for i in range(m - 2):
        for j in range(n - 2):
            for k in range(i + 1, m - 1):
                for l in range(j + 1, n - 1):
                    if np.sum(matrix[i:k + 1, j:l + 1]) == 411:
                        submatrices.append(matrix[i:k + 1, j:l + 1])
    return submatrices