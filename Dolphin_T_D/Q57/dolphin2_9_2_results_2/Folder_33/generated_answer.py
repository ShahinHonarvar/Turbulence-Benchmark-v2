import numpy as np

def submatrix_with_particular_sum(matrix):
    subs = []
    n, m = matrix.shape
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    sum = np.sum(matrix[i:k + 1, j:l + 1])
                    if sum == -811:
                        subs.append(matrix[i:k + 1, j:l + 1])
    return subs if subs else []