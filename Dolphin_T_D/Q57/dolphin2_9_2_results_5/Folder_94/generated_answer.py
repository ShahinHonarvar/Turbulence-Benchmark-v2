import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    result = []
    for i in range(m):
        for j in range(n):
            if i > j:
                for x in range(i + 1, m):
                    for y in range(j + 1, n):
                        submatrix = matrix[i:x, j:y]
                        if np.sum(submatrix) == 92:
                            result.append(submatrix.tolist())
    return result