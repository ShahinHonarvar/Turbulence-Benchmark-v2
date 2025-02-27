import numpy as np

def submatrix_with_particular_sum(mat):
    result = []
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            for k in range(i, mat.shape[0]):
                for l in range(j, mat.shape[1]):
                    if np.sum(mat[i:k + 1, j:l + 1]) == 16:
                        result.append(mat[i:k + 1, j:l + 1].tolist())
    return result