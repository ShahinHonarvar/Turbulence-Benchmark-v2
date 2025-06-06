import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for k in range(i + 1, rows):
                for l in range(j + 1, cols):
                    submatrix_sum = np.sum(matrix[i:k, j:l])
                    if submatrix_sum == -97:
                        submatrices.append(matrix[i:k, j:l])
    return submatrices