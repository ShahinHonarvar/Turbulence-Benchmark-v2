import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(m, n):
        submats = []
        for row_start in range(m):
            for row_end in range(row_start, m):
                for col_start in range(n):
                    for col_end in range(col_start, n):
                        submat = matrix[row_start:row_end + 1, col_start:col_end + 1]
                        if np.sum(submat) == -936:
                            submats.append(submat)
        return submats
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        return []
    m, n = matrix.shape
    return get_submatrices(m, n)