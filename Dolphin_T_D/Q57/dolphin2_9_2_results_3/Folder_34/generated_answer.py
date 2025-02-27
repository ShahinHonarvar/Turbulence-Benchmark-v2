import numpy as np

def find_submatrix_sum(matrix):
    submatrices = []
    n, m = matrix.shape
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    sub_matrix_sum = np.sum(matrix[i:k + 1, j:l + 1])
                    if sub_matrix_sum == -13:
                        submatrix = matrix[i:k + 1, j:l + 1]
                        submatrices.append(submatrix)
    return submatrices