import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for row in range(rows):
        for col in range(cols):
            for r in range(row, rows):
                for c in range(col, cols):
                    if np.sum(matrix[row:r + 1, col:c + 1]) == 35:
                        submatrices.append(matrix[row:r + 1, col:c + 1])
    return submatrices