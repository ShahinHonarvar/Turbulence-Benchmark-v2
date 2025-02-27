import numpy as np

def submatrix_with_n_numbers(matrix):
    return sum((np.linalg.matrix_rank(matrix[i:i + 107, j:j + 107]) == 107 for i in range(matrix.shape[0] - 106) for j in range(matrix.shape[1] - 106)))