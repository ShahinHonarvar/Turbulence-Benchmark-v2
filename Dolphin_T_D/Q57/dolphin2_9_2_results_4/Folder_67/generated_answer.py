import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    matrix_size = len(matrix)
    for i in range(matrix_size):
        for j in range(matrix_size):
            for k in range(i + 1, matrix_size):
                for l in range(j + 1, matrix_size):
                    submatrix = matrix[i:k, j:l]
                    if np.sum(submatrix) == 40:
                        submatrices.append(submatrix)
    if submatrices:
        return submatrices
    else:
        return []