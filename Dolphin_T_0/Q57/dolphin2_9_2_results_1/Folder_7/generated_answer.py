import numpy as np

def submatrix_with_particular_sum(mat):
    result = []
    h, w = mat.shape
    for i in range(h):
        for j in range(w):
            for k in range(i + 1, h):
                for l in range(j + 1, w):
                    submat = mat[i:k, j:l]
                    if np.sum(submat) == -128:
                        result.append(submat.tolist())
    return result