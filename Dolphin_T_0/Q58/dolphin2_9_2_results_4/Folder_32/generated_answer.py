import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    matrix_rows, matrix_cols = matrix.shape
    for i in range(matrix_rows):
        for j in range(matrix_cols):
            for k in range(i, matrix_rows):
                for l in range(j, matrix_cols):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if np.count_nonzero(submatrix) == 103:
                        submatrix_count += 1
    if submatrix_count == 0:
        return 0
    else:
        return submatrix_count