import numpy as np

def submatrix_with_particular_sum(matrix):
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    submatrices = []
    for row in range(rows):
        for col in range(cols):
            for row_end in range(row, rows):
                for col_end in range(col, cols):
                    submatrix = matrix[row:row_end + 1, col:col_end + 1]
                    if submatrix.sum() == 56:
                        submatrices.append(submatrix)
    return submatrices