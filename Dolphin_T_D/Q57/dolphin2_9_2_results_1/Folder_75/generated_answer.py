import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    matrix_size = len(matrix)
    for i in range(matrix_size):
        for j in range(matrix_size):
            for k in range(i, matrix_size):
                for l in range(j, matrix_size):
                    submatrix_values = matrix[i:k + 1, j:l + 1]
                    if np.sum(submatrix_values) == 16:
                        result.append(submatrix_values)
    return result