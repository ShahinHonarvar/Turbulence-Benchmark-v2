import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for row_start in range(matrix.shape[0]):
        for col_start in range(matrix.shape[1]):
            for row_end in range(row_start, matrix.shape[0]):
                for col_end in range(col_start, matrix.shape[1]):
                    submatrix = matrix[row_start:row_end + 1, col_start:col_end + 1]
                    if np.sum(submatrix) == 394:
                        submatrices.append(submatrix)
    return submatrices