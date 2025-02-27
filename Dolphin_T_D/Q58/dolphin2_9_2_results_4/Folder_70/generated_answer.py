import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    matrix_rows, matrix_cols = matrix.shape
    for i in range(matrix_rows - 2):
        for j in range(matrix_cols - 2):
            count = 0
            submatrix = matrix[i:i + 3, j:j + 3]
            for row in submatrix:
                count += sum(row == 173)
            if count == 3:
                submatrix_count += 1
    return submatrix_count