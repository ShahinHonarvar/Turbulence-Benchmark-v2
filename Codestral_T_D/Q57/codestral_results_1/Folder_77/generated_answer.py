import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for r in range(i, rows):
                for c in range(j, cols):
                    submatrix = matrix[i:r + 1, j:c + 1]
                    if submatrix.sum() == -336:
                        submatrices.append(submatrix)
    return submatrices