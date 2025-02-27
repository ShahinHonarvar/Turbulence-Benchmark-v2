import numpy as np

def submatrix_with_particular_sum(matrix):
    sum_to_find = 901
    submatrices = []
    shape = matrix.shape
    for i in range(shape[0]):
        for j in range(shape[1]):
            for r in range(i, shape[0]):
                for c in range(j, shape[1]):
                    if np.sum(matrix[i:r + 1, j:c + 1]) == sum_to_find:
                        submatrices.append(matrix[i:r + 1, j:c + 1])
    return submatrices