import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for size_i in range(i, matrix.shape[0] + 1):
                for size_j in range(j, matrix.shape[1] + 1):
                    sub_matrix_sum = np.sum(matrix[i:size_i, j:size_j])
                    if sub_matrix_sum == 78:
                        submatrices.append(matrix[i:size_i, j:size_j])
    return submatrices