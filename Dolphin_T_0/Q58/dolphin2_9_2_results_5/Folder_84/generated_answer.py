import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    return sum((1 for i in range(m - 3) for j in range(n - 3) if sum(matrix[i:i + 4, j:j + 4].flatten()) == 127))