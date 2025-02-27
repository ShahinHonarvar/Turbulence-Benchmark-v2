import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 39 + 1):
        for j in range(matrix.shape[1] - 39 + 1):
            submatrix = matrix[i:i + 39, j:j + 39]
            if np.all(submatrix == 39):
                count += 1
    return count