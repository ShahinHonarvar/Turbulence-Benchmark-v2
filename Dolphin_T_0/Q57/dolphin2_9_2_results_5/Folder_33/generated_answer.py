import numpy as np

def submatrix_with_particular_sum(matrix):
    n, m = matrix.shape
    submatrices = []
    for i in range(n):
        for j in range(m):
            for k in range(i + 1, n + 1):
                for l in range(j + 1, m + 1):
                    sub_matrix = matrix[i:k, j:l]
                    if np.sum(sub_matrix) == -811:
                        submatrices.append(sub_matrix)
    return submatrices