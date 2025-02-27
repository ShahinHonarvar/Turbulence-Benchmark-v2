import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 103
    m, _ = matrix.shape
    count = 0
    for i in range(m - n + 1):
        for j in range(m - n + 1):
            submatrix = matrix[i:i + n, j:j + n]
            if np.all(submatrix == 103):
                count += 1
    return count