import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    n, m = matrix.shape
    for i in range(n):
        for j in range(m):
            for k1 in range(i + 1, n + 1):
                for l1 in range(j + 1, m + 1):
                    sub_mat = matrix[i:k1, j:l1]
                    if np.sum(sub_mat) == 21:
                        result.append(sub_mat)
    return result