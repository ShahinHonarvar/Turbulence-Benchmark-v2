import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            for x in range(i, n):
                for y in range(j, m):
                    if np.sum(matrix[i:x + 1, j:y + 1]) == 2:
                        submatrices.append(matrix[i:x + 1, j:y + 1])
    return submatrices