import numpy as np

def submatrix_with_particular_sum(matrix):
    row, col = matrix.shape
    submatrix_list = []
    for i in range(row):
        for j in range(col):
            for k in range(i, row):
                for l in range(j, col):
                    sub_mat = matrix[i:k + 1, j:l + 1]
                    if np.sum(sub_mat) == 69:
                        submatrix_list.append(sub_mat)
    return submatrix_list