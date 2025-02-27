import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    result = []
    for i in range(m):
        for j in range(n):
            for k in range(i + 1, m):
                for l in range(j + 1, n):
                    submatrix = np.array(matrix[i:k, j:l])
                    if np.sum(submatrix) == -63:
                        result.append(submatrix.tolist())
    return result