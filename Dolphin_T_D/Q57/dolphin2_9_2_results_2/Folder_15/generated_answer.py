import numpy as np

def submatrix_with_particular_sum(matrix):
    n, m = matrix.shape
    submatrices = []
    for i in range(n):
        for j in range(m):
            for k in range(i + 1, n + 1):
                for l in range(j + 1, m + 1):
                    submatrix_sum = np.sum(matrix[i:k, j:l])
                    if submatrix_sum == -9:
                        submatrices.append(matrix[i:k, j:l])
    return submatrices