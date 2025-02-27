import numpy as np

def submatrix_with_particular_sum(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    submatrices = []
    for i in range(rows):
        for j in range(cols):
            for r in range(i, rows):
                for c in range(j, cols):
                    submatrix = matrix[i:r + 1, j:c + 1]
                    if np.sum(submatrix) == 830:
                        submatrices.append(submatrix.tolist())
    return submatrices