import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    row, column = matrix.shape
    for i in range(row):
        for j in range(column):
            for x in range(i + 1, row + 1):
                for y in range(j + 1, column + 1):
                    subset = matrix[i:x, j:y]
                    if np.sum(subset) == 15:
                        submatrices.append(subset)
    return submatrices