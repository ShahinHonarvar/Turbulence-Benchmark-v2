import numpy as np

def submatrix_with_particular_sum(matrix):
    sum = 40
    n = len(matrix)
    m = len(matrix[0])
    submatrices = []
    for i in range(n):
        for j in range(m):
            for x in range(i, n):
                for y in range(j, m):
                    sub = np.array(matrix[i:x + 1, j:y + 1])
                    if np.sum(sub) == sum:
                        submatrices.append(sub)
    return submatrices