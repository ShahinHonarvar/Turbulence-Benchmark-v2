from numpy import *

def submatrix_with_particular_sum(matrix):
    n, m = matrix.shape
    for i in range(n):
        for j in range(i, n):
            for k in range(m):
                for l in range(k, m):
                    submatrix = matrix[i:j + 1, k:l + 1]
                    if submatrix.sum() == 100:
                        return submatrix.tolist()
    return []