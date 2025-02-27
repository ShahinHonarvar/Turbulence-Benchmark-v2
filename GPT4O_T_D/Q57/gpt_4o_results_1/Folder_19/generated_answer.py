import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(mat, row_start, row_end, col_start, col_end):
        total = 0
        for row in range(row_start, row_end + 1):
            for col in range(col_start, col_end + 1):
                total += mat[row, col]
        return total
    num_rows, num_cols = matrix.shape
    result = []
    for row_start in range(num_rows):
        for row_end in range(row_start, num_rows):
            for col_start in range(num_cols):
                for col_end in range(col_start, num_cols):
                    if submatrix_sum(matrix, row_start, row_end, col_start, col_end) == -97:
                        submatrix = matrix[row_start:row_end + 1, col_start:col_end + 1]
                        result.append(submatrix)
    return result