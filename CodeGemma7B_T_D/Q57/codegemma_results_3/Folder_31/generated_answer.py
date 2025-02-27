import numpy as np

def submatrix_with_particular_sum(matrix):
    results = []
    for r in range(matrix.shape[0]):
        for c in range(matrix.shape[1]):
            for r2 in range(r, matrix.shape[0]):
                for c2 in range(c, matrix.shape[1]):
                    temp = matrix[r:r2 + 1, c:c2 + 1]
                    if temp.sum() == -44:
                        results.append(temp)
    return results