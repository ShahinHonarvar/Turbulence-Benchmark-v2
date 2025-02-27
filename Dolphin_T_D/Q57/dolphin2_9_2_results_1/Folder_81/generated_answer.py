import numpy as np

def submatrix_with_particular_sum(matrix):
    n, m = matrix.shape
    submatrices = []
    for i in range(n):
        for j in range(m):
            for p in range(i, n):
                for q in range(j, m):
                    if np.sum(matrix[i:p + 1, j:q + 1]) == -90:
                        submatrices.append(matrix[i:p + 1, j:q + 1])
    return submatrices