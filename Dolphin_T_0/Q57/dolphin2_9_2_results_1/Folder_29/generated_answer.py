import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    submatrices = []
    for i in range(m + 1):
        for j in range(n + 1):
            for k in range(i, m + 1):
                for l in range(j, n + 1):
                    if i != k and j != l:
                        s = np.sum(matrix[i:k, j:l])
                        if s == 84:
                            submatrices.append(matrix[i:k, j:l])
    if not submatrices:
        return []
    return submatrices