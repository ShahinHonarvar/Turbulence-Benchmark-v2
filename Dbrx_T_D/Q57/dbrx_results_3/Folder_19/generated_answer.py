import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices_sum_equal_to_negative_ninety_seven = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if np.sum(submatrix) == -97:
                        submatrices_sum_equal_to_negative_ninety_seven.append(submatrix)
    if not submatrices_sum_equal_to_negative_ninety_seven:
        return []
    else:
        return submatrices_sum_equal_to_negative_ninety_seven