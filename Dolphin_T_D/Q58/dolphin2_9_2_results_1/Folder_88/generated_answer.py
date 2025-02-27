import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    return sum((matrix[i:i + 3, j:j + 3].sum() == 67 for i in range(m - 2) for j in range(n - 2)))