import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices_sum_394 = []
    rows, cols = matrix.shape
    for row_start in range(rows):
        for row_end in range(row_start, rows):
            for col_start in range(cols):
                for col_end in range(col_start, cols):
                    submatrix = matrix[row_start:row_end + 1, col_start:col_end + 1]
                    if submatrix.sum() == -394:
                        submatrices_sum_394.append(submatrix)
    if not submatrices_sum_394:
        return []
    else:
        return submatrices_sum_394