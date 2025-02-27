import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    height, width = matrix.shape
    for i in range(height):
        for j in range(width):
            for k in range(height - i):
                for l in range(width - j):
                    submatrix_sum = np.sum(matrix[i:i + k, j:j + l])
                    if submatrix_sum == 997:
                        submatrices.append(matrix[i:i + k, j:j + l])
    return submatrices