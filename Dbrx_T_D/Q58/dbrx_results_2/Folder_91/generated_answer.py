import numpy as np

def submatrix_with_n_numbers(matrix):
    n, m = matrix.shape
    count = 0
    for i in range(n - 4):
        for j in range(m - 4):
            submatrix = matrix[i:i + 5, j:j + 5]
            if np.all(submatrix == 5):
                count += 1
    return count