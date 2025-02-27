import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(matrix, row_start, row_end, col_start, col_end):
        return np.sum(matrix[row_start:row_end + 1, col_start:col_end + 1])
    rows, cols = matrix.shape
    submatrices = []
    for row_start in range(rows):
        for row_end in range(row_start, rows):
            for col_start in range(cols):
                for col_end in range(col_start, cols):
                    if submatrix_sum(matrix, row_start, row_end, col_start, col_end) == 77:
                        submatrices.append(matrix[row_start:row_end + 1, col_start:col_end + 1].tolist())
    return submatrices