import numpy as np

def find_submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    submatrices = []
    for i in range(m):
        for j in range(n):
            for k in range(i, m):
                for l in range(j, n):
                    submatrix_sum = np.sum(matrix[i:k + 1, j:l + 1])
                    if submatrix_sum == 56:
                        submatrix = matrix[i:k + 1, j:l + 1]
                        submatrices.append(submatrix)
    return submatrices