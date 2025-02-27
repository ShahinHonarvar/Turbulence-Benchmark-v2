import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    size = matrix.shape[0]
    for i in range(size):
        for j in range(size):
            for row in range(i, size):
                for col in range(j, size):
                    submatrix = matrix[i:row + 1, j:col + 1]
                    if np.sum(submatrix) == -50:
                        submatrices.append(submatrix.tolist())
    return submatrices