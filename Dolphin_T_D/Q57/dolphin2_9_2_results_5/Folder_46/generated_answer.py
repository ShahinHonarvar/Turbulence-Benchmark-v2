import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    size = matrix.shape[0]
    for i in range(size):
        for j in range(size):
            for i2 in range(i, size):
                for j2 in range(j, size):
                    submatrix_sum = int(np.sum(matrix[i:i2 + 1, j:j2 + 1]))
                    if submatrix_sum == 416:
                        submatrices.append(matrix[i:i2 + 1, j:j2 + 1])
    return submatrices