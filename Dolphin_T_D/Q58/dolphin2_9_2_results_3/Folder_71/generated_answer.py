import numpy as np

def submatrix_with_n_numbers(matrix):
    counter = 0
    matrix_rows, matrix_cols = matrix.shape
    for i in range(matrix_rows):
        for j in range(matrix_cols):
            for x in range(i + 1, matrix_rows + 1):
                for y in range(j + 1, matrix_cols + 1):
                    if np.sum(matrix[i:x, j:y]) == 78:
                        counter += 1
    if counter == 0:
        return 0
    else:
        return counter