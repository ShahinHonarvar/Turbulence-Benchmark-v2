import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    submatrices = []
    for i in range(m):
        for j in range(n):
            for test_m in range(i + 1, m + 1):
                for test_n in range(j + 1, n + 1):
                    partial_matrix = matrix[i:test_m, j:test_n]
                    if np.sum(partial_matrix) == 616:
                        submatrices.append(partial_matrix.tolist())
    return submatrices