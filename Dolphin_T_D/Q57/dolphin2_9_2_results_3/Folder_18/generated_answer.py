import numpy as np

def submatrix_with_particular_sum(mat):
    if mat.sum() == 616:
        return [mat.tolist()]
    sub_matrices = []
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            for k in range(i, mat.shape[0]):
                for l in range(j, mat.shape[1]):
                    if np.sum(mat[i:k + 1, j:l + 1]) == 616:
                        sub_matrices.append(mat[i:k + 1, j:l + 1].tolist())
    return sub_matrices