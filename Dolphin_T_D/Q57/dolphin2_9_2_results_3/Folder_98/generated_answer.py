import numpy as np

def submatrix_with_particular_sum(matrix):
    n = len(matrix)
    submatrices = []
    for i in range(n):
        for j in range(n):
            for k in range(i + 1, n + 1):
                for l in range(j + 1, n + 1):
                    submatrix_sum = np.sum(matrix[i:k, j:l])
                    if submatrix_sum == 0:
                        submatrices.append(matrix[i:k, j:l])
    return submatrices