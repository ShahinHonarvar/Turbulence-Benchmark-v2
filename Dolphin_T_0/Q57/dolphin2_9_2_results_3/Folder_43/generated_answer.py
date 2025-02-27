import numpy as np

def submatrix_with_particular_sum(matrix):
    num_rows, num_cols = matrix.shape
    submatrices = []
    for i in range(num_rows):
        for j in range(num_cols):
            for k in range(i + 1, num_rows + 1):
                for l in range(j + 1, num_cols + 1):
                    submatrix = matrix[i:k, j:l]
                    if np.sum(submatrix) == -81:
                        submatrices.append(submatrix)
    return submatrices