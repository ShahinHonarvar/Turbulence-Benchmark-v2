import numpy as np

def submatrix_with_particular_sum(matrix):
    n, m = matrix.shape
    submatrices = []
    for i in range(n - 1):
        for j in range(m - 1):
            submatrix_sum = matrix[i:i + 2, j:j + 2].sum()
            if submatrix_sum == 8:
                submatrices.append(matrix[i:i + 2, j:j + 2])
    return submatrices