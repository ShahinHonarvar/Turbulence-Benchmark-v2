import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for size_one in range(1, min(matrix.shape[0] - i, matrix.shape[1] - j) + 1):
                for size_two in range(1, min(matrix.shape[0] - i, matrix.shape[1] - j) + 1):
                    submatrix = matrix[i:i + size_one, j:j + size_two]
                    if np.sum(submatrix) == 27:
                        submatrices.append(submatrix)
    return submatrices