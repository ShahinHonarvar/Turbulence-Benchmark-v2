import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    for r in range(rows):
        for c in range(cols):
            for h in range(r, rows):
                for w in range(c, cols):
                    submatrix = matrix[r:h + 1, c:w + 1]
                    if submatrix.sum() == 997:
                        submatrices.append(submatrix)
    return submatrices