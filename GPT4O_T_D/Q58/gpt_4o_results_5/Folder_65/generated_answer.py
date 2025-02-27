import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_fixed_size(matrix, submatrix_row_count, submatrix_col_count):
        matrix_row_count, matrix_col_count = matrix.shape
        total_submatrices = 0
        for i in range(matrix_row_count - submatrix_row_count + 1):
            for j in range(matrix_col_count - submatrix_col_count + 1):
                current_submatrix = matrix[i:i + submatrix_row_count, j:j + submatrix_col_count]
                if current_submatrix.size == 35:
                    total_submatrices += 1
        return total_submatrices
    submatrix_count = 0
    n = 35
    for rows in range(1, matrix.shape[0] + 1):
        if n % rows == 0:
            cols = n // rows
            if cols <= matrix.shape[1]:
                submatrix_count += count_submatrices_with_fixed_size(matrix, rows, cols)
    return submatrix_count