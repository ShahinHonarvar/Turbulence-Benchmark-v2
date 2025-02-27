import numpy as np

def submatrix_with_particular_sum(matrix):
    if not isinstance(matrix, np.ndarray):
        raise ValueError('Input matrix must be a numpy array')
    if matrix.ndim != 2:
        raise ValueError('Input matrix must be 2-dimensional')
    submatrices_with_sum_54 = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if np.sum(submatrix) == 54:
                        submatrices_with_sum_54.append(submatrix.tolist())
    return submatrices_with_sum_54