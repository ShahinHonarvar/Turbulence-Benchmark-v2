import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    n, m = matrix.shape
    for i in range(n):
        for j in range(m):
            for x in range(i + 1, n + 1):
                for y in range(j + 1, m + 1):
                    submatrix = np.array(matrix[i:x, j:y])
                    if submatrix.sum() == 382:
                        submatrices.append(submatrix.tolist())
    return submatrices