import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    submatrices = []
    for i in range(m):
        for j in range(n):
            for x in range(i, m):
                for y in range(j, n):
                    sub = np.sum(matrix[i:x + 1, j:y + 1])
                    if sub == 92:
                        submatrices.append(matrix[i:x + 1, j:y + 1])
    return submatrices