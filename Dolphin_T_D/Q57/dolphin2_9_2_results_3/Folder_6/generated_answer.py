import numpy as np

def submatrix_with_particular_sum(matrix):
    n = len(matrix)
    m = len(matrix[0])
    submatrices = []
    for i in range(n):
        for j in range(m):
            for k in range(i + 1, n + 1):
                for l in range(j + 1, m + 1):
                    sub = np.sum(matrix[i:k, j:l])
                    if sub == 126:
                        submatrices.append(matrix[i:k, j:l])
    return submatrices if submatrices else []