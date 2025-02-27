import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for row in range(rows):
        for col in range(cols):
            for height in range(row, rows):
                for width in range(col, cols):
                    submatrix = matrix[row:height + 1, col:width + 1]
                    if np.sum(submatrix) == -42:
                        submatrices.append(submatrix)
    return submatrices