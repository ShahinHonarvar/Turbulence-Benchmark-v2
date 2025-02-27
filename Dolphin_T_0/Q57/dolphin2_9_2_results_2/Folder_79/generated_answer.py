import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    N = len(matrix[0])
    for i in range(len(matrix)):
        for j in range(N):
            for x in range(i, len(matrix)):
                for y in range(j, N):
                    if np.sum(matrix[i:x + 1, j:y + 1]) == -47:
                        submatrices.append(matrix[i:x + 1, j:y + 1])
    return submatrices