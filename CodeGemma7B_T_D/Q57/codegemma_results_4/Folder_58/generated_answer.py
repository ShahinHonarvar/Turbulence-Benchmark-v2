import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[1]):
            for r in range(row + 1):
                for c in range(col + 1):
                    submatrix = matrix[r:row + 1, c:col + 1]
                    if submatrix.sum() == -137:
                        submatrices.append((r, row, c, col))
    return submatrices