import numpy as np

def submatrix_with_particular_sum(matrix):
    return [matrix[i:i + r, j:j + c] for i in range(matrix.shape[0]) for j in range(matrix.shape[1]) for r in range(1, matrix.shape[0] - i + 1) for c in range(1, matrix.shape[1] - j + 1) if np.sum(matrix[i:i + r, j:j + c]) == 93]