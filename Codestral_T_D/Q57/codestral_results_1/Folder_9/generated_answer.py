import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    for r in range(rows):
        for c in range(cols):
            for h in range(r + 1, rows + 1):
                for w in range(c + 1, cols + 1):
                    submatrix = matrix[r:h, c:w]
                    if np.sum(submatrix) == -86:
                        submatrices.append(submatrix)
    return submatrices