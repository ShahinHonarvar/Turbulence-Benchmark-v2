import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices_sum_equal_to_77 = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if np.sum(submatrix) == -77:
                        submatrices_sum_equal_to_77.append(submatrix)
    if submatrices_sum_equal_to_77:
        return submatrices_sum_equal_to_77
    else:
        return []