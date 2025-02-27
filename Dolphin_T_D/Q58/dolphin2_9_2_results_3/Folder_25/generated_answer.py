import numpy as np

def submatrix_with_n_numbers(matrix):
    total = 0
    m, n = matrix.shape
    for i in range(m - 2):
        for j in range(n - 2):
            if 66 in matrix[i:i + 3, j:j + 3]:
                total += 1
    return total