import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices_sum_equal_to_minus_47 = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows + 1):
                for l in range(j, cols + 1):
                    submatrix = matrix[i:k, j:l]
                    if submatrix.sum() == -47:
                        submatrices_sum_equal_to_minus_47.append(submatrix)
    return submatrices_sum_equal_to_minus_47