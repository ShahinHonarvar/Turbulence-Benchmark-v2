import numpy as np

def submatrix_with_particular_sum(mat):
    rows = len(mat)
    cols = len(mat[0])
    submatrices = []
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    part = np.array(mat[i:k + 1, j:l + 1])
                    if np.sum(part) == 38:
                        submatrices.append(part)
    return submatrices