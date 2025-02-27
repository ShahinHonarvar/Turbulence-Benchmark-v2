import numpy as np

def submatrix_with_particular_sum(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        return []
    shape = matrix.shape
    result_matrix = np.zeros((shape[0], shape[1]))
    for i in range(shape[0]):
        for j in range(shape[1]):
            for k in range(i + 1, shape[0]):
                for l in range(j + 1, shape[1]):
                    submatrix = matrix[i:k, j:l]
                    if np.sum(submatrix) == 56:
                        result_matrix[i, j] = 1
    return result_matrix