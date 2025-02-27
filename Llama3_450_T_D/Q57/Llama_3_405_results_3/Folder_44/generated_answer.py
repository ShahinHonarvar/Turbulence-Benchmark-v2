import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(matrix):
        rows, cols = matrix.shape
        for row_start in range(rows):
            for col_start in range(cols):
                for row_end in range(row_start + 1, rows + 1):
                    for col_end in range(col_start + 1, cols + 1):
                        yield matrix[row_start:row_end, col_start:col_end]
    return [submatrix for submatrix in get_submatrices(matrix) if np.sum(submatrix) == 830]