import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for row in range(i, matrix.shape[0]):
                for col in range(j, matrix.shape[1]):
                    submatrix_sum = np.sum(matrix[i:row + 1, j:col + 1])
                    if submatrix_sum == 15:
                        submatrices.append(matrix[i:row + 1, j:col + 1])
    return submatrices