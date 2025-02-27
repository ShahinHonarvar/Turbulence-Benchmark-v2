import numpy as np

def submatrix_with_particular_sum(matrix):
    row_num, col_num = matrix.shape
    submatrices = []
    for i in range(row_num):
        for j in range(col_num):
            for k in range(i, row_num):
                for l in range(j, col_num):
                    sub_matrix = matrix[i:k + 1, j:l + 1]
                    if np.sum(sub_matrix) == 40:
                        submatrices.append(sub_matrix)
    return submatrices