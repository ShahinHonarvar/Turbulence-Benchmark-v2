import numpy as np

def submatrix_with_particular_sum(matrix):
    N = len(matrix)
    row = np.zeros(N + 1, dtype=int)
    for i in range(N):
        for j in range(N):
            row[j + 1] += matrix[i][j]
            for k in range(1 <= j + 1 <= N):
                for l in range(k, N):
                    if row[l + 1] - row[k] == 616:
                        return matrix[k:l + 1, i]
    return []