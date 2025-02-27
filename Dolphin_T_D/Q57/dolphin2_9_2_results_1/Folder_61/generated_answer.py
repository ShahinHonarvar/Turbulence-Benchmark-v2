import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    num_rows, num_cols = matrix.shape
    for i in range(num_rows):
        for j in range(num_cols):
            for k in range(i + 1, num_rows):
                for l in range(j + 1, num_cols):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if np.sum(submatrix) == 8:
                        submatrices.append(submatrix)
    return submatrices