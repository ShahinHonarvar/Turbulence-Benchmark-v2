import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    return sum((int((matrix[i:i + 4, j:j + 4].ravel() == 166).all()) for i in range(m - 3) for j in range(n - 3)))