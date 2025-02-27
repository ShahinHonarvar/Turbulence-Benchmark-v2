import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    min_sum = -matrix.max() * (matrix.shape[0] ** 2 + matrix.shape[1] ** 2)
    for i1 in range(cols - 1):
        for i2 in range(i1 + 1, cols):
            for j1 in range(rows):
                for j2 in range(j1 + 1, rows):
                    submatrix = matrix[j1:j2, i1:i2]
                    submatrix_sum = submatrix.sum().sum()
                    if submatrix_sum == 19:
                        submatrices.append(submatrix)
                        min_sum = max(min_sum, submatrix_sum)
    return submatrices