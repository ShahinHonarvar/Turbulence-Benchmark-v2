import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    height, width = matrix.shape
    for i in range(height - 2):
        for j in range(width - 2):
            submatrix = matrix[i:i + 3, j:j + 3]
            if np.all(submatrix == 8):
                submatrix_count += 1
    return submatrix_count