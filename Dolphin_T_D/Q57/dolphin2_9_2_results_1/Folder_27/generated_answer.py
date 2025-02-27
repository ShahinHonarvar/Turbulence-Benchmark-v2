import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    result = []
    for i in range(m):
        for j in range(n):
            for x in range(i, m):
                for y in range(j, n):
                    if np.sum(matrix[i:x + 1, j:y + 1]) == 77:
                        result.append(matrix[i:x + 1, j:y + 1])
    return result