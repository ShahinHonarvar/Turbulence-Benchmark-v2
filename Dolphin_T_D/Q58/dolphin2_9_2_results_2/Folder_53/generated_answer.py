import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    size = matrix.size
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if size - i - matrix.shape[1] >= 24 and size - j - matrix.shape[0] >= 24:
                submatrix = matrix[i:i + 4, j:j + 6]
                if np.all(submatrix == 24):
                    count += 1
    return count if count > 0 else 0