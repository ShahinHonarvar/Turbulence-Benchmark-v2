import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            for k in range(i, n):
                for l in range(j, n):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if np.sum(submatrix) == 35:
                        submatrices.append(submatrix)
    return submatrices