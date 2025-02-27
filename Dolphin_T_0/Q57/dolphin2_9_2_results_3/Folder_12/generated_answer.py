import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    N, M = matrix.shape
    P = matrix.sum()
    target = -83
    for u in range(N - 1):
        for d in range(M - 1):
            for v in range(u + 1, N):
                for w in range(d + 1, M):
                    S = matrix[u:v + 1, d:w + 1].sum()
                    if S == target:
                        result.append(matrix[u:v + 1, d:w + 1].tolist())
    return result