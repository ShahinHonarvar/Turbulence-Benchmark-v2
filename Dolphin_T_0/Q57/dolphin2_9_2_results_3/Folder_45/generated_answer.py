import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    submatrices = []
    for i in range(m):
        for j in range(n):
            for k in range(i + 1, m + 1):
                for l in range(j + 1, n + 1):
                    sub_matrix = matrix[i:k, j:l]
                    if np.sum(sub_matrix) == -77:
                        submatrices.append(sub_matrix)
    return submatrices