import numpy as np

def submatrix_with_n_numbers(matrix):
    height, width = matrix.shape
    n = 41
    count = 0
    for i in range(height - n + 1):
        for j in range(width - n + 1):
            submatrix = matrix[i:i + n, j:j + n]
            if np.all(submatrix == 41):
                count += 1
    return count