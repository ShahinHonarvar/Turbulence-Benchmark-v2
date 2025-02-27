import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2 or matrix.dtype.kind != 'i':
        return 0
    m, n = matrix.shape
    count = 0
    for i in range(m - 1):
        for j in range(n - 1):
            submatrix = matrix[i:i + 2, j:j + 2]
            if len(submatrix) == 4 and len(submatrix[0]) == 2 and (len(submatrix[1]) == 2):
                if len(submatrix.flatten()) == 127:
                    count += 1
    return count