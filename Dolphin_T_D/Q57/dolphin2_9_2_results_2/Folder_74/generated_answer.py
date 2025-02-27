import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    m, n = matrix.shape
    for x in range(m):
        for y in range(n):
            for x1 in range(x, m):
                for y1 in range(y, n):
                    sub = np.array(matrix[x:x1 + 1, y:y1 + 1])
                    if np.sum(sub) == 88:
                        submatrices.append(sub)
    return submatrices