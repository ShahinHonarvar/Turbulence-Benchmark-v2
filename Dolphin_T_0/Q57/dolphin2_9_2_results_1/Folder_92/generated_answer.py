import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    n, m = matrix.shape
    for i in range(n):
        for j in range(m):
            for x in range(i, n):
                for y in range(j, m):
                    submatrix = matrix[i:x + 1, j:y + 1]
                    if submatrix.sum() == -3:
                        submatrices.append(submatrix.tolist())
    return submatrices