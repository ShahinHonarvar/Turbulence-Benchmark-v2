import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i + 3 < len(matrix) and j + 3 < len(matrix[0]):
                if np.sum(matrix[i:i + 3, j:j + 3]) == 64:
                    submatrices.append(matrix[i:i + 3, j:j + 3])
    return submatrices