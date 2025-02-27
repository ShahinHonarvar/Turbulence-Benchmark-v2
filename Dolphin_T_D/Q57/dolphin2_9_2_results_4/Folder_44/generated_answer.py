import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    n, m = matrix.shape
    for i in range(n):
        for j in range(m):
            for z in range(i + 1, n + 1):
                for w in range(j + 1, m + 1):
                    if np.sum(matrix[i:z, j:w]) == 830:
                        result.append(matrix[i:z, j:w])
    return result