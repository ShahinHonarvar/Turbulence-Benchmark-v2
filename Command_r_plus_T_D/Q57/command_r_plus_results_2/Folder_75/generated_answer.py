import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            for x in range(rows - i + 1):
                for y in range(cols - j + 1):
                    submatrix = matrix[x:x + i, y:y + j]
                    if np.sum(submatrix) == 16:
                        submatrices.append(submatrix)
    return submatrices