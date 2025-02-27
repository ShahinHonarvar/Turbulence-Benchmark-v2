import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for i in range(rows):
        for j in range(cols):
            for x in range(i + 1, rows + 1):
                for y in range(j + 1, cols + 1):
                    if sum(matrix[i:x, j:y]) == -36:
                        submatrices.append(matrix[i:x, j:y])
    return submatrices