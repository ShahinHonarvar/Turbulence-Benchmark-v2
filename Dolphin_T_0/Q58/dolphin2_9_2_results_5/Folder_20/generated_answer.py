import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    height, width = matrix.shape
    for i in range(height - 4):
        for j in range(width - 4):
            submatrix = matrix[i:i + 5, j:j + 5]
            if np.all(submatrix == 49):
                count += 1
    return count