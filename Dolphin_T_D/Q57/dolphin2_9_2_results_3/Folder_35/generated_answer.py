import numpy as np

def submatrix_with_particular_sum(matrix):
    N = len(matrix)
    M = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            if i == 0 or j == 0:
                M[i, j] = matrix[i, j]
            else:
                M[i, j] = matrix[i, j] + M[i - 1, j] + M[i, j - 1] - M[i - 1, j - 1]
    submatrices = []
    for i in range(N):
        for j in range(N):
            for k in range(i, N):
                for l in range(j, N):
                    if M[k, l] - M[k, j - 1] - M[i - 1, l] + M[i - 1, j - 1] == 432:
                        submatrices.append(matrix[i:k + 1, j:l + 1])
    return submatrices