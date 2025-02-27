import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrix_sum(mat, start_row, start_col, end_row, end_col):
        return mat[start_row:end_row, start_col:end_col].sum()
    nrows, ncols = matrix.shape
    submatrices = []
    for start_row in range(nrows):
        for start_col in range(ncols):
            for end_row in range(start_row + 1, nrows + 1):
                for end_col in range(start_col + 1, ncols + 1):
                    if get_submatrix_sum(matrix, start_row, start_col, end_row, end_col) == -185:
                        submatrices.append(matrix[start_row:end_row, start_col:end_col].copy())
    return submatrices