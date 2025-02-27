import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(i + 1, rows + 1):
            for k in range(cols):
                for l in range(k + 1, cols + 1):
                    submatrix = matrix[i:j, k:l]
                    if submatrix.sum() == -83:
                        result.append(submatrix)
    return result