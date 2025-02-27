import numpy as np

def submatrix_with_particular_sum(matrix):
    n, m = matrix.shape
    result = []
    for i in range(n):
        for j in range(m):
            for k in range(i + 1, n):
                for l in range(j + 1, m):
                    submatrix_sum = np.sum(matrix[i:k, j:l])
                    if submatrix_sum == -3:
                        result.append(matrix[i:k, j:l])
    return result