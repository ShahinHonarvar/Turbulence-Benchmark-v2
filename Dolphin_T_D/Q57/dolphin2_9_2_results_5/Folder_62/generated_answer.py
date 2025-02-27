import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for row_size in range(1, matrix.shape[0] - i + 1):
                for col_size in range(1, matrix.shape[1] - j + 1):
                    submatrix = matrix[i:i + row_size, j:j + col_size]
                    if np.sum(submatrix) == 394:
                        submatrices.append(submatrix)
    return submatrices