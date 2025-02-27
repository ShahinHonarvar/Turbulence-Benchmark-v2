import numpy as np

def submatrix_with_particular_sum(matrix):
    N = len(matrix[0])
    submatrices = []
    for i in range(len(matrix) - 1):
        for j in range(N - 1):
            for k in range(i, len(matrix)):
                for l in range(j, N):
                    tmp = np.array(matrix[i:k + 1, j:l + 1])
                    if np.sum(tmp) == 411:
                        submatrices.append(tmp.tolist())
    return submatrices