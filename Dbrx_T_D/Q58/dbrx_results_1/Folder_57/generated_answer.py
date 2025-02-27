import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    for i in range(matrix.shape[0] - 1):
        for j in range(matrix.shape[1] - 1):
            submatrix = matrix[i:i + 92, j:j + 92]
            if submatrix.shape == (92, 92):
                if np.all(submatrix == 92):
                    submatrix_count += 1
    return submatrix_count