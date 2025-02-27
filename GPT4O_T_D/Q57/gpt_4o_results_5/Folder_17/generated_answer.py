import numpy as np

def submatrix_with_particular_sum(matrix):

    def sum_submatrix(r1, c1, r2, c2):
        return np.sum(matrix[r1:r2 + 1, c1:c2 + 1])
    submatrices = []
    rows, cols = matrix.shape
    for row_start in range(rows):
        for row_end in range(row_start, rows):
            for col_start in range(cols):
                for col_end in range(col_start, cols):
                    if sum_submatrix(row_start, col_start, row_end, col_end) == 398:
                        submatrices.append(matrix[row_start:row_end + 1, col_start:col_end + 1].tolist())
    return submatrices