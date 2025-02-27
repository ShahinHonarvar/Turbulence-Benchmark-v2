import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices_sum_35 = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if np.sum(submatrix) == 35:
                        submatrices_sum_35.append(submatrix)
    return submatrices_sum_35