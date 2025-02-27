import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    K = 35
    submatrices = []
    for r in range(m):
        for c in range(n):
            for i in range(r, m):
                for j in range(c, n):
                    sum = int(np.sum(matrix[r:i + 1, c:j + 1]))
                    if sum == K:
                        submatrix = matrix[r:i + 1, c:j + 1].tolist()
                        submatrices.append(submatrix)
    return submatrices