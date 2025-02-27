import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    height, width = matrix.shape
    for i in range(height - 3):
        for j in range(width - 3):
            submatrix = matrix[i:i + 4, j:j + 4]
            if np.all(submatrix == 96):
                count += 1
    return count