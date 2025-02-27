import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for size_i in range(i + 1, matrix.shape[0] + 1):
                for size_j in range(j + 1, matrix.shape[1] + 1):
                    sub_matrix = matrix[i:size_i, j:size_j]
                    if np.sum(sub_matrix) == -394:
                        submatrices.append(sub_matrix)
    return submatrices