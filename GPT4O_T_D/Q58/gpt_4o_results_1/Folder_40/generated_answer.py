import numpy as np

def submatrix_with_n_numbers(matrix):

    def contains_only_ones(submatrix):
        return np.all(submatrix == 1)

    def count_one_by_one_matrices(matrix):
        rows, cols = matrix.shape
        count = 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i, j] == 1:
                    count += 1
        return count
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        raise ValueError('Input must be a 2D numpy matrix.')
    return count_one_by_one_matrices(matrix)