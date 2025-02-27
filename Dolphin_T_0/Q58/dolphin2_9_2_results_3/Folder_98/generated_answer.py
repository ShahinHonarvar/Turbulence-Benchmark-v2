import numpy as np

def submatrix_with_n_numbers(mat):
    if not isinstance(mat, np.ndarray) or mat.ndim != 2:
        return 0
    m, n = mat.shape
    count = 0
    for i in range(1 + m - 3):
        for j in range(1 + n - 3):
            if np.all(np.array_equal(mat[i:i + 3, j:j + 3], mat[i, j:j + 3])) and np.all(np.array_equal(mat[i:i + 3, j:j + 3], mat[i:j + 3, j])):
                count += 1
    return count