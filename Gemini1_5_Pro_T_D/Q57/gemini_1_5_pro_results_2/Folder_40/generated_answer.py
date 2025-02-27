import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            for r in range(i + 1, rows + 1):
                for c in range(j + 1, cols + 1):
                    submatrix = matrix[i:r, j:c]
                    if np.sum(submatrix) == -10:
                        submatrices.append(submatrix.tolist())
    return submatrices