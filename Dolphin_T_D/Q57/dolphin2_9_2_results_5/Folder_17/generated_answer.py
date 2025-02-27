import numpy as np

def submatrix_with_particular_sum(matrix):
    r, c = matrix.shape
    submatrices = []
    for i in range(r - 2):
        for j in range(c - 2):
            for i2 in range(i + 1, r - 1):
                for j2 in range(j + 1, c - 1):
                    if matrix[i:i2 + 1, j:j2 + 1].sum() == 398:
                        submatrices.append(matrix[i:i2 + 1, j:j2 + 1])
    return submatrices