import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        return 0
    n = matrix.shape[0] * matrix.shape[1]
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    if len(submatrices) < n:
                        submatrix = matrix[i:k + 1, j:l + 1]
                        if submatrix.size == 1:
                            submatrices.append(submatrix)
                    else:
                        break
            if len(submatrices) >= n:
                break
    return len(submatrices)