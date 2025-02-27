import numpy as np

def submatrix_with_particular_sum(matrix):
    n = matrix.shape[0]
    m = matrix.shape[1]
    result = []
    for i in range(n):
        for j in range(n):
            for k in range(i + 1, n):
                for l in range(j + 1, m):
                    temp = matrix[i:k + 1, j:l + 1]
                    if temp.sum() == 126:
                        result.append(temp)
    return result