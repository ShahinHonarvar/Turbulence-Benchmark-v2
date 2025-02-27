import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for r in range(rows):
        for c in range(cols):
            for i in range(r + 1):
                for j in range(c + 1):
                    if np.sum(matrix[i:r + 1, j:c + 1]) == -13:
                        submatrices.append(matrix[i:r + 1, j:c + 1])
    return submatrices