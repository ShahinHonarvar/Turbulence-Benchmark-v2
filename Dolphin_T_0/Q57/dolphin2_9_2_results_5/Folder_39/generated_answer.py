import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    sums = matrix.sum(axis=(1, 2))
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    if matrix[k, l].sum() - matrix[i, j].sum() == 66:
                        submatrices.append(matrix[i:k + 1, j:l + 1])
    return submatrices