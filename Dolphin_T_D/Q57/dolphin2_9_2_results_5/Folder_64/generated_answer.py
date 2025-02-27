import numpy as np

def submatrix_with_particular_sum(mat):
    rows, cols = mat.shape
    submatrices = []
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    sub_sum = np.sum(mat[i:k + 1, j:l + 1])
                    if sub_sum == -4:
                        submatrices.append(mat[i:k + 1, j:l + 1])
    return submatrices