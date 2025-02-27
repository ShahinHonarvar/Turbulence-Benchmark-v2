import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i + 1 < len(matrix) and j + 1 < len(matrix[0]):
                if np.sum(matrix[i:i + 2, j:j + 2]) == -44:
                    result.append(matrix[i:i + 2, j:j + 2])
    return result