import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for i in range(rows):
        for j in range(cols):
            for x in range(i, rows):
                for y in range(j, cols):
                    submatrix_sum = np.sum(matrix[i:x + 1, j:y + 1])
                    if submatrix_sum == 99:
                        submatrices.append(matrix[i:x + 1, j:y + 1])
    return submatrices