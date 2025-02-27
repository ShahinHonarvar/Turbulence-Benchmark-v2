import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    m, n = matrix.shape
    for i in range(m):
        for j in range(n):
            for h in range(i, m):
                for w in range(j, n):
                    submatrix = matrix[i:h + 1, j:w + 1]
                    if np.sum(submatrix) == 87:
                        submatrices.append(submatrix.tolist())
    return submatrices