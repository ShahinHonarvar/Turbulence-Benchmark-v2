import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    height, width = matrix.shape
    for i in range(height):
        for j in range(width):
            for h in range(i, height):
                for w in range(j, width):
                    submatrix = matrix[i:h + 1, j:w + 1]
                    if np.sum(submatrix) == -65:
                        submatrices.append(submatrix.tolist())
    return submatrices