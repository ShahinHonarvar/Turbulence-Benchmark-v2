import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for x in range(i + 1, matrix.shape[0] + 1):
                for y in range(j + 1, matrix.shape[1] + 1):
                    sub_matrix = matrix[i:x, j:y].sum()
                    if sub_matrix == -59:
                        submatrices.append(matrix[i:x, j:y].tolist())
    return submatrices