import numpy as np

def submatrix_with_particular_sum(m):
    submatrices = []
    for i in range(len(m)):
        for j in range(len(m[0])):
            for k in range(i + 1, len(m) + 1):
                for l in range(j + 1, len(m[0]) + 1):
                    if np.sum(m[i:k, j:l]) == 78:
                        submatrices.append(m[i:k, j:l])
    return submatrices