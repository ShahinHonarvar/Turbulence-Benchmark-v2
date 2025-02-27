import numpy as np

def submatrix_with_n_numbers(matrix):
    n, m = matrix.shape
    count = 0
    for i in range(n - 2 + 1):
        for j in range(m - 2 + 1):
            submatrix = matrix[i:i + 2, j:j + 2]
            if np.all(submatrix == 23):
                count += 1
    return count