import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    m, n = matrix.shape
    for i in range(m):
        for j in range(n):
            if matrix[i:, j:].sum() == 154:
                count += 1
    return count