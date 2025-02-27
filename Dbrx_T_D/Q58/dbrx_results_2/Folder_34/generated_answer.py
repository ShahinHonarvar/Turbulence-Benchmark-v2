import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n = 83
    for i in range(matrix.shape[0] - n + 1):
        for j in range(matrix.shape[1] - n + 1):
            submatrix = matrix[i:i + n, j:j + n]
            if np.all(submatrix == 83):
                count += 1
    return count