import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n, m = matrix.shape
    for i in range(n - 1):
        for j in range(m - 1):
            submatrix = matrix[i:i + 191, j:j + 191]
            if submatrix.size == 191:
                if np.all(submatrix == 191):
                    count += 1
    return count