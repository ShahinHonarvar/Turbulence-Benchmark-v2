import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(matrix):
        rows, cols = matrix.shape
        submatrices = []
        for r1 in range(rows):
            for r2 in range(r1, rows):
                for c1 in range(cols):
                    for c2 in range(c1, cols):
                        submatrix = matrix[r1:r2 + 1, c1:c2 + 1]
                        if np.sum(submatrix) == 99:
                            submatrices.append(submatrix)
        return submatrices
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        raise ValueError('Input must be a two-dimensional numpy array')
    return get_submatrices(matrix)