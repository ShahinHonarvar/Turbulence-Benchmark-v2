import numpy as np

def submatrix_with_particular_sum(matrix):
    row, col = matrix.shape
    sub_matrices = []
    for i in range(row):
        for j in range(col):
            for k in range(i, row):
                for l in range(j, col):
                    sub = matrix[i:k + 1, j:l + 1]
                    if np.sum(sub) == -4:
                        sub_matrices.append(sub.tolist())
    return sub_matrices