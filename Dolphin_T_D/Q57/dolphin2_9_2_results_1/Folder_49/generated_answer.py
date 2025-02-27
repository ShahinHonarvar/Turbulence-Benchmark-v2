import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    matrix = np.array(matrix)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for size in range(min(matrix.shape[0] - i + 1, matrix.shape[1] - j + 1)):
                submatrix_sum = np.sum(matrix[i:i + size, j:j + size])
                if submatrix_sum == -42:
                    submatrices.append(matrix[i:i + size, j:j + size].tolist())
    return submatrices