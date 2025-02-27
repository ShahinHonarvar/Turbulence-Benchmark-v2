import numpy as np

def submatrix_with_particular_sum(matrix):
    list_of_submatrices = []
    matrix_size = np.size(matrix)
    for i in range(matrix_size):
        for j in range(matrix_size):
            for k in range(i + 1, matrix_size + 1):
                for l in range(j + 1, matrix_size + 1):
                    submatrix = matrix[i:k, j:l]
                    if np.sum(submatrix) == -863:
                        list_of_submatrices.append(submatrix)
    return list_of_submatrices