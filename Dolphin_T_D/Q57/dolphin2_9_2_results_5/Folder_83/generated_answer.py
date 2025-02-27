import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    row, col = matrix.shape
    matrix_elements = matrix.flatten()
    for i in range(row):
        for j in range(col):
            for x in range(i, row):
                for y in range(j, col):
                    submatrix = matrix[i:x + 1, j:y + 1]
                    if np.sum(submatrix) == -15:
                        submatrices.append(submatrix.tolist())
    return submatrices