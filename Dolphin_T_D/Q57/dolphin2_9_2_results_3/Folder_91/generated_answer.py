import numpy as np

def submatrix_with_particular_sum(matrix):
    N = len(matrix)
    M = len(matrix[0])
    submatrices = []
    for i in range(N):
        for j in range(M):
            for k in range(i, N):
                for l in range(j, M):
                    gross_sum = np.sum(matrix[i:k + 1, j:l + 1])
                    if gross_sum == -6:
                        cur_submatrix = matrix[i:k + 1, j:l + 1]
                        submatrices.append(cur_submatrix.tolist())
    return submatrices