import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    target_sum = -936
    submatrices = []
    for row_start in range(rows):
        for col_start in range(cols):
            for row_end in range(row_start, rows):
                for col_end in range(col_start, cols):
                    submatrix = matrix[row_start:row_end + 1, col_start:col_end + 1]
                    if np.sum(submatrix) == target_sum:
                        submatrices.append(submatrix.copy())
    return submatrices