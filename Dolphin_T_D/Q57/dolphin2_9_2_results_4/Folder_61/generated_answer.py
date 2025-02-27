import numpy as np

def submatrix_with_particular_sum(matrix):
    size = matrix.shape[0]
    submatrices = []
    for i in range(size):
        for j in range(size):
            for x in range(i + 1, size + 1):
                for y in range(j + 1, size + 1):
                    if matrix[i:x, j:y].sum() == 8:
                        submatrices.append(matrix[i:x, j:y].tolist())
    return submatrices