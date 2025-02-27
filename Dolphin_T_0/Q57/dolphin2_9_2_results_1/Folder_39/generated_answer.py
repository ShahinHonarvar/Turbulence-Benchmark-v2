import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for i in range(rows - 1):
        for j in range(cols - 1):
            for x in range(i + 1, rows):
                for y in range(j + 1, cols):
                    submatrix = matrix[i:x + 1, j:y + 1]
                    if submatrix.sum() == 66:
                        submatrices.append(submatrix)
    return submatrices