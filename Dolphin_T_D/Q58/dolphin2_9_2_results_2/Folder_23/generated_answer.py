import numpy as np

def submatrix_with_n_numbers(matrix, n=69):
    if not isinstance(matrix, np.ndarray):
        raise typeError('Input must be numpy array')
    if any((isinstance(i, list) for i in matrix)):
        matrix = np.array(matrix)
    if matrix.ndim != 2:
        raise ValueError('Input must be a two-dimensional numpy array')
    if not all((isinstance(i, int) for i in matrix.flatten())):
        raise ValueError('All elements of the matrix must be integers')
    h, w = matrix.shape
    count = 0
    for i in range(h - n + 1):
        for j in range(w - n + 1):
            if np.count_nonzero(matrix[i:i + n, j:j + n] == n) == n * n:
                count += 1
    return count