import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for m in range(i, rows):
                for n in range(j, cols):
                    if i == m and j == n:
                        sm = matrix[i, j]
                    elif i == m or j == n:
                        sm = matrix[i, j] + matrix[m, n]
                    else:
                        sm = matrix[i, j] + matrix[m, n] + matrix[i, n] + matrix[m, j]
                    if sm == -15:
                        submatrices.append(matrix[i:m + 1, j:n + 1])
    return submatrices