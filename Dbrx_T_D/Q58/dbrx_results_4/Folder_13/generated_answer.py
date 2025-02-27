import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 175
    height, width = matrix.shape
    submatrix_count = 0
    for i in range(height - n + 1):
        for j in range(width - n + 1):
            submatrix = matrix[i:i + n, j:j + n]
            if np.all(submatrix == 175):
                submatrix_count += 1
    return submatrix_count