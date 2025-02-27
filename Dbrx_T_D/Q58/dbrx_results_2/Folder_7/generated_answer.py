import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 121
    height, width = matrix.shape
    count = 0
    for i in range(height - n + 1):
        for j in range(width - n + 1):
            submatrix = matrix[i:i + n, j:j + n]
            if np.all(submatrix == n):
                count += 1
    return count