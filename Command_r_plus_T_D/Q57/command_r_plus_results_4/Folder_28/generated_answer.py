import numpy as np

def submatrix_with_particular_sum(matrix: np.ndarray) -> list[np.ndarray]:
    if not isinstance(matrix, np.ndarray):
        raise TypeError('Input must be a numpy ndarray.')
    if matrix.ndim != 2:
        raise ValueError('Input must be a 2D matrix.')
    if not np.issubdtype(matrix.dtype, np.integer):
        raise TypeError('Input matrix must contain only integers.')

    def get_submatrices(matrix, row_start, row_end, col_start, col_end):
        return matrix[row_start:row_end, col_start:col_end]

    def get_all_submatrices(matrix):
        submatrices = []
        for row_start in range(matrix.shape[0]):
            for row_end in range(row_start + 1, matrix.shape[0] + 1):
                for col_start in range(matrix.shape[1]):
                    for col_end in range(col_start + 1, matrix.shape[1] + 1):
                        submatrices.append(get_submatrices(matrix, row_start, row_end, col_start, col_end))
        return submatrices

    def sum_of_submatrix(submatrix):
        return np.sum(submatrix)
    all_submatrices = get_all_submatrices(matrix)
    submatrices_with_sum_15 = [submatrix for submatrix in all_submatrices if sum_of_submatrix(submatrix) == 15]
    return submatrices_with_sum_15