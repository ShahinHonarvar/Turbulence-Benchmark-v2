import numpy as np

def submatrix_with_particular_sum(matrix):
    n, m = matrix.shape
    submatrices = []
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for x in range(0, n - i + 1):
                for y in range(0, m - j + 1):
                    if np.sum(matrix[x:x + i, y:y + j]) == -61:
                        submatrices.append(matrix[x:x + i, y:y + j])
    return submatrices