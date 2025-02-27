import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    for row in range(rows):
        for col in range(cols):
            for i in range(row, rows):
                for j in range(col, cols):
                    submatrix = matrix[row:i + 1, col:j + 1]
                    if np.sum(submatrix) == -9:
                        submatrices.append(submatrix)
    return submatrices