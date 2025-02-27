import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    s = np.sum(matrix)
    matrix = np.array(matrix)
    m, n = np.shape(matrix)
    for I in range(m):
        for J in range(n):
            for i in range(I + 1, m + 1):
                for j in range(J + 1, n + 1):
                    sub = np.sum(matrix[i - 1:i, j - 1:j]) + np.sum(matrix[I:i, J:j]) - np.sum(matrix[I:i, j - 1:j]) - np.sum(matrix[i - 1:i, J:j])
                    if sub == 94:
                        submatrices.append(matrix[I:i, J:j])
    return submatrices