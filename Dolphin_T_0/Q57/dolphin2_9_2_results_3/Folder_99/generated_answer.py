import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    matrix_size = len(matrix)
    for row_start in range(0, matrix_size):
        for col_start in range(0, matrix_size):
            for row_end in range(row_start, matrix_size):
                for col_end in range(col_start, matrix_size):
                    if np.sum(matrix[row_start:row_end + 1, col_start:col_end + 1]) == -185:
                        submatrices.append(matrix[row_start:row_end + 1, col_start:col_end + 1])
    return submatrices