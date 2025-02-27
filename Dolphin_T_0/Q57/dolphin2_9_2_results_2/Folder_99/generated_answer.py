import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrix_list = []
    m, n = matrix.shape
    for i in range(m):
        for j in range(n):
            for k in range(i, m):
                for l in range(j, n):
                    submatrix_sum = np.sum(matrix[i:k + 1, j:l + 1])
                    if submatrix_sum == -185:
                        submatrix_list.append(matrix[i:k + 1, j:l + 1])
    return submatrix_list