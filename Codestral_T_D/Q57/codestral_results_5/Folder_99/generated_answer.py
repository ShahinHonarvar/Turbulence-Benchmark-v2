import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for r in range(rows):
        for c in range(cols):
            for h in range(r + 1, rows + 1):
                for w in range(c + 1, cols + 1):
                    submatrix = matrix[r:h, c:w]
                    if np.sum(submatrix) == -185:
                        submatrices.append(submatrix)
    return submatrices