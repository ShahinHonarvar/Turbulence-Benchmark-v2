import numpy as np

def submatrix_with_particular_sum(matrix):
    if isinstance(matrix, np.ndarray) and matrix.ndim == 2 and (matrix.dtype == np.int32):
        submatrices = []
        for h in range(matrix.shape[0]):
            for w in range(matrix.shape[1]):
                for h2 in range(h + 1, matrix.shape[0] + 1):
                    for w2 in range(w + 1, matrix.shape[1] + 1):
                        sub = matrix[h:h2, w:w2]
                        if np.sum(sub) == -13:
                            submatrices.append(sub)
        return submatrices
    else:
        raise ValueError('Input must be a two-dimensional numpy matrix of integers')