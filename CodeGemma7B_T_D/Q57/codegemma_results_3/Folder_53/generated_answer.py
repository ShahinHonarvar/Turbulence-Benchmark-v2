import numpy as np

def submatrix_with_particular_sum(matrix):
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    result = []
    for i in range(rows):
        for j in range(i, rows):
            for k in range(cols):
                for l in range(k, cols):
                    submatrix = matrix[i:j + 1, k:l + 1]
                    if submatrix.sum() == -37:
                        result.append(submatrix)
    return result