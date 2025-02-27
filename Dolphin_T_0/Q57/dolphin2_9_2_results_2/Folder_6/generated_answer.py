import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    height, width = matrix.shape
    for i in range(height):
        for j in range(width):
            for h in range(i + 1, height + 1):
                for w in range(j + 1, width + 1):
                    submatrix = matrix[i:h, j:w]
                    if np.sum(submatrix) == 126:
                        submatrices.append(submatrix)
    return submatrices