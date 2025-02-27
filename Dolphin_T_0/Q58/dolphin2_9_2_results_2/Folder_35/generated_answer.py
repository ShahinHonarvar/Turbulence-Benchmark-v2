import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2 or (not all((isinstance(i, int) for i in matrix.flatten()))):
        return 0
    m, n = matrix.shape
    count = 0
    for i in range(m - 2):
        for j in range(n - 2):
            if np.all(matrix[i:i + 3, j:j + 3] == 111):
                count += 1
    return count