import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    m, n = matrix.shape
    for i in range(m - 3):
        for j in range(n - 3):
            submatrix = matrix[i:i + 4, j:j + 4]
            if submatrix.shape == (4, 4) and np.count_nonzero(submatrix == 17) == 16:
                count += 1
    return count