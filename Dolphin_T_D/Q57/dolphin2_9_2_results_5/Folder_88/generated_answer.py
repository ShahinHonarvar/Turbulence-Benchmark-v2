import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    height, width = matrix.shape
    for i in range(height):
        for j in range(width):
            for end_i in range(i, height):
                for end_j in range(j, width):
                    submatrix = matrix[i:end_i + 1, j:end_j + 1]
                    if np.sum(submatrix) == -64:
                        result.append(submatrix)
    return result