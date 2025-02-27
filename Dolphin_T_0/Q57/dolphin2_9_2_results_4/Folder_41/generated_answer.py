import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, columns = matrix.shape
    submatrices = []
    for i in range(rows):
        for j in range(columns):
            for k in range(i + 1, rows + 1):
                for l in range(j + 1, columns + 1):
                    submatrix = matrix[i:k, j:l]
                    if np.sum(submatrix) == -26:
                        submatrices.append(submatrix)
    return submatrices