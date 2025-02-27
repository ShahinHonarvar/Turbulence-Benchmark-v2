import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for row_length in range(1, matrix.shape[0] - i + 1):
                for col_length in range(1, matrix.shape[1] - j + 1):
                    submatrix_sum = np.sum(matrix[i:i + row_length, j:j + col_length])
                    if submatrix_sum == 99:
                        submatrices.append(matrix[i:i + row_length, j:j + col_length])
    return submatrices