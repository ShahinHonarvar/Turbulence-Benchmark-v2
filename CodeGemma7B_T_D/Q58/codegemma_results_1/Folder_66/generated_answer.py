import numpy as np

def submatrix_with_n_numbers(matrix):
    """Return the number of submatrix which have 42 integer in it."""
    if not isinstance(matrix, np.ndarray):
        raise TypeError('Matrix is not a numpy array')
    value = 42
    max_num = matrix.shape[0]
    return len([(i, j, k, l) for i in range(max_num) for j in range(max_num) for k in range(i + 1, max_num + 1) for l in range(j + 1, max_num + 1) if (matrix[i:k, j:l] == value).all()])