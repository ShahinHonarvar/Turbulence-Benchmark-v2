import numpy as np

def submatrix_with_particular_sum(matrix):
    M, N = matrix.shape
    res = []
    for i in range(M):
        for j in range(N):
            for k in range(i, M):
                for l in range(j, N):
                    if i == k and j == l:
                        if sum(matrix[i, j]) == -811:
                            res.append(matrix[i:k + 1, j:l + 1])
                    elif sum(matrix[i:k + 1, j:l + 1]) == -811:
                        res.append(matrix[i:k + 1, j:l + 1])
    return res