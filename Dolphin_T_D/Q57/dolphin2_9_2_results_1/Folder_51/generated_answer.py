import numpy as np

def submatrix_with_particular_sum(mat):
    result = []
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            for k in range(i + 1, len(mat) + 1):
                for n in range(j + 1, len(mat[0]) + 1):
                    if np.sum(mat[i:k, j:n]) == -46:
                        result.append(mat[i:k, j:n])
    return result