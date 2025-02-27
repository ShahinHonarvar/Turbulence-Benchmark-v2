import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    submatrix_sum = np.sum(matrix[i:k, j:l])
                    if submatrix_sum == -336:
                        submatrix = matrix[i:k, j:l]
                        submatrices.append(submatrix)
    return submatrices