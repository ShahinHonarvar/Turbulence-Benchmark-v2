import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    submatrix_list = []
    for i in range(m):
        for j in range(n):
            for k in range(i, m):
                for l in range(j, n):
                    sub_matrix = matrix[i:k + 1, j:l + 1]
                    if sub_matrix.sum() == -47:
                        submatrix_list.append(sub_matrix.tolist())
    return submatrix_list