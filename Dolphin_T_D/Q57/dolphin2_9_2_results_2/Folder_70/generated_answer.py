import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    submatrices = []
    for i in range(m):
        for j in range(n):
            for r in range(i, m):
                for c in range(j, n):
                    if np.sum(matrix[i:r + 1, j:c + 1]) == 411:
                        submatrices.append(matrix[i:r + 1, j:c + 1].tolist())
    return submatrices