import numpy as np

def submatrix_with_particular_sum(matrix):
    output = []
    m, n = matrix.shape
    for i in range(m):
        for j in range(n):
            for t in range(i + 1, m + 1):
                for s in range(j + 1, n + 1):
                    submatrix = matrix[i:t, j:s]
                    if -97 in submatrix.sum():
                        output.append(submatrix)
                        break
    return output