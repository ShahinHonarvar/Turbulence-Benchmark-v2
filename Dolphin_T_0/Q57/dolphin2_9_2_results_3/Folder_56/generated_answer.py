import numpy as np

def submatrix_with_particular_sum(matrix):
    row, col = matrix.shape
    sub_list = []
    for i in range(row):
        for j in range(col):
            for k in range(i, row):
                for l in range(j, col):
                    if np.sum(matrix[i:k + 1, j:l + 1]) == -50:
                        sub_list.append(matrix[i:k + 1, j:l + 1])
    return sub_list