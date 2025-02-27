import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for size in range(min(len(matrix) - i, len(matrix[0]) - j), 0, -1):
                submatrix_sum = np.sum(matrix[i:i + size, j:j + size])
                if submatrix_sum == -25:
                    submatrices.append(matrix[i:i + size, j:j + size])
    return submatrices