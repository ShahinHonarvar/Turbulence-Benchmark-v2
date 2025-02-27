import numpy as np

def submatrix_with_particular_sum(matrix):
    N = len(matrix)
    submatrices = []
    for x in range(N):
        for y in range(N):
            for z in range(x, N):
                for w in range(y, N):
                    if np.sum(matrix[x:z + 1, y:w + 1]) == -27:
                        submatrices.append(matrix[x:z + 1, y:w + 1])
    return submatrices