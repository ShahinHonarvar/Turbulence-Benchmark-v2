import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(matrix.shape[0] + 1):
        for j in range(matrix.shape[1] + 1):
            for p in range(matrix.shape[0] - i + 1):
                for q in range(matrix.shape[1] - j + 1):
                    submatrix = matrix[i:i + p, j:j + q]
                    if np.sum(submatrix) == -97:
                        submatrices.append(submatrix)
    return submatrices if submatrices else []