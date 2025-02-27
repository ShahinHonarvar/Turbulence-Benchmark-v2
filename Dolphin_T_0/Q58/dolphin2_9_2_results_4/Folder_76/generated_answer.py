import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 159
    return sum((1 for i in range(matrix.shape[0]) for j in range(matrix.shape[1]) for x in range(i + 1, matrix.shape[0]) for y in range(j + 1, matrix.shape[1]) if (x - i + 1) * (y - j + 1) == n and np.sum(matrix[i:x + 1, j:y + 1]) == n))