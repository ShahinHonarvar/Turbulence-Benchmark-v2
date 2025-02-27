import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices_sum_equal_to_negative_38 = []
    height, width = matrix.shape
    for i in range(height):
        for j in range(width):
            for k in range(i, height):
                for l in range(j, width):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if np.sum(submatrix) == -38:
                        submatrices_sum_equal_to_negative_38.append(submatrix)
    if submatrices_sum_equal_to_negative_38:
        return submatrices_sum_equal_to_negative_38
    else:
        return []