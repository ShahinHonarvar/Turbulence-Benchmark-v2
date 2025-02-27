import numpy as np

def submatrix_with_particular_sum(matrix):
    n, m = matrix.shape
    submatrices = []
    for i in range(n):
        for j in range(m):
            for u in range(i + 1, n):
                for v in range(j + 1, m):
                    partial_matrix = matrix[i:u, j:v]
                    if np.sum(partial_matrix) == -59 and partial_matrix.shape != matrix.shape:
                        submatrices.append(partial_matrix)
    return submatrices if len(submatrices) else []