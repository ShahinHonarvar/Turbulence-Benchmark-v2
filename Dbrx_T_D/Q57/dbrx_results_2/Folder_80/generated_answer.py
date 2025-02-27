import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices_with_sum_245 = []
    for i in range(matrix.shape[0] - 1):
        for j in range(matrix.shape[1] - 1):
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    current_submatrix = matrix[i:k + 1, j:l + 1]
                    if np.sum(current_submatrix) == 245:
                        submatrices_with_sum_245.append(current_submatrix)
    if submatrices_with_sum_245:
        return submatrices_with_sum_245
    else:
        return []