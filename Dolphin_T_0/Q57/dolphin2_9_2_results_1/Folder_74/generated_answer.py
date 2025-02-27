import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for size_i in range(1, matrix.shape[0] - i + 1):
                for size_j in range(1, matrix.shape[1] - j + 1):
                    submatrix_sum = np.sum(matrix[i:i + size_i, j:j + size_j])
                    if submatrix_sum == 88:
                        submatrix = matrix[i:i + size_i, j:j + size_j]
                        submatrices.append(submatrix.tolist())
    return submatrices