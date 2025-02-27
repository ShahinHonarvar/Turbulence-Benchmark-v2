import numpy as np

def submatrix_with_particular_sum(matrix):
    size = matrix.shape
    result = []
    for i in range(size[0]):
        for j in range(i, size[0]):
            for k in range(size[1]):
                for l in range(k, size[1]):
                    if matrix[i:j + 1, k:l + 1].sum() == 77:
                        result.append(matrix[i:j + 1, k:l + 1])
    return result