import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    for i in range(rows):
        for j in range(cols):
            for k in range(i + 1, rows + 1):
                for l in range(j + 1, cols + 1):
                    submatrix_sum = np.sum(matrix[i:k, j:l])
                    if submatrix_sum == -10:
                        submatrices.append(matrix[i:k, j:l])
    return submatrices