import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    matrix_rows, matrix_cols = matrix.shape
    for i in range(matrix_rows - 2):
        for j in range(matrix_cols - 2):
            is_submatrix = True
            for k in range(3):
                for l in range(3):
                    if matrix[i + k][j + l] != 13:
                        is_submatrix = False
                        break
                if not is_submatrix:
                    break
            if is_submatrix:
                submatrix_count += 1
    return submatrix_count