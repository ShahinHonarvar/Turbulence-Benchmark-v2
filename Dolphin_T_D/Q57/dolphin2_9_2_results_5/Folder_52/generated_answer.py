import numpy as np

def submatrix_with_particular_sum(matrix):
    n, m = matrix.shape
    submatrices = []
    for x in range(n // 2):
        for y in range(m // 2):
            if matrix[x][y] + matrix[x][y + 1] + matrix[x + 1][y] + matrix[x + 1][y + 1] == 100:
                submatrix = matrix[x:x + 2, y:y + 2]
                submatrices.append(submatrix.tolist())
    return submatrices