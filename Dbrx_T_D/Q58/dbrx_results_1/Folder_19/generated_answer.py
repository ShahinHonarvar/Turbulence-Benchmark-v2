import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 17
    if matrix.shape[0] < n or matrix.shape[1] < n:
        return 0
    count = 0
    for row_start in range(matrix.shape[0] - n + 1):
        for row_end in range(row_start + n):
            for col_start in range(matrix.shape[1] - n + 1):
                for col_end in range(col_start + n):
                    submatrix = matrix[row_start:row_end, col_start:col_end]
                    if np.isin(submatrix, 17).all():
                        count += 1
    return count