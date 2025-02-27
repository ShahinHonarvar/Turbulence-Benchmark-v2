import numpy as np

def submatrix_with_particular_sum(matrix):
    return [matrix[i:i + m, j:j + n] for i in range(matrix.shape[0]) for j in range(matrix.shape[1]) if np.sum(matrix[i:i + m, j:j + n]) == 100]