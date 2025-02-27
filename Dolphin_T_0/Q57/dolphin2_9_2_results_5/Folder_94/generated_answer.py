import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    matrix_size = matrix.shape
    for i in range(matrix_size[0]):
        for j in range(matrix_size[1]):
            for row in range(i + 1, matrix_size[0] + 1):
                for col in range(j + 1, matrix_size[1] + 1):
                    submatrix_sum = np.sum(matrix[i:row, j:col])
                    if submatrix_sum == 92:
                        result.append(matrix[i:row, j:col])
    return result