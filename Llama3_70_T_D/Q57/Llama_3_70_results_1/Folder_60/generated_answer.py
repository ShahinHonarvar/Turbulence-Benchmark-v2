import numpy as np

def submatrix_with_particular_sum(matrix):
    n, m = matrix.shape
    result = []
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for last_column in range(j, m):
                    sub = matrix[i:k + 1, j:last_column + 1]
                    if np.sum(sub) == 94:
                        result.append(sub.tolist())
    return result