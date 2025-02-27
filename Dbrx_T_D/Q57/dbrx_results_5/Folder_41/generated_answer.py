import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices_sum_eq_min = []
    rows, cols = matrix.shape
    for row in range(rows):
        for col in range(cols):
            for row_length in range(1, rows + 1 - row):
                for col_length in range(1, cols + 1 - col):
                    submatrix = matrix[row:row + row_length, col:col + col_length]
                    if submatrix.sum() == -26:
                        submatrices_sum_eq_min.append(submatrix)
    return submatrices_sum_eq_min