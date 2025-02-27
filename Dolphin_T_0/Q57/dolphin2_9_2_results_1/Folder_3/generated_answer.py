import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for r in range(rows):
        for c in range(cols):
            for dr in range(r, rows):
                for dc in range(c, cols):
                    if np.sum(matrix[r:dr + 1, c:dc + 1]) == 54:
                        submatrices.append(matrix[r:dr + 1, c:dc + 1])
    return submatrices