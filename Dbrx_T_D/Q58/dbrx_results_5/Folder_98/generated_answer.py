import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n = 3
    height, width = matrix.shape
    for i in range(height - n + 1):
        for j in range(width - n + 1):
            submatrix = matrix[i:i + n, j:j + n]
            if np.all(submatrix == 9):
                count += 1
    return count