import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    zero_sum_submatrices = []
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows + 1):
                for l in range(j, cols + 1):
                    submatrix = matrix[i:k, j:l]
                    if np.sum(submatrix) == 0 and submatrix.size > 1:
                        zero_sum_submatrices.append(submatrix)
    return zero_sum_submatrices