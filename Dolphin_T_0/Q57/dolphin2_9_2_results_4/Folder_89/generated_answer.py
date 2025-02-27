import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    matrix_size = matrix.shape[0]
    for l in range(matrix_size):
        for m in range(matrix_size):
            for n in range(matrix_size):
                if l <= n < m and n + (n - l + 1) <= m + 1 and (sum(matrix[l:n + 1, m:n + 1].flatten()) == 80):
                    submatrices.append(matrix[l:n + 1, m:n + 1])
    return submatrices