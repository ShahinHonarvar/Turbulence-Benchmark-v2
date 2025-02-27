import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    for i in range(matrix.shape[0] - 179):
        for j in range(matrix.shape[1] - 179):
            submatrix = matrix[i:i + 180, j:j + 180]
            if np.all(submatrix == 180):
                submatrix_count += 1
    return submatrix_count