import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(mat, start_row, start_col, rows, cols):
        return np.sum(mat[start_row:start_row + rows, start_col:start_col + cols])
    n, m = matrix.shape
    result = []
    for start_row in range(n):
        for start_col in range(m):
            for end_row in range(start_row, n):
                for end_col in range(start_col, m):
                    if submatrix_sum(matrix, start_row, start_col, end_row - start_row + 1, end_col - start_col + 1) == 100:
                        submatrix = matrix[start_row:end_row + 1, start_col:end_col + 1].copy()
                        result.append(submatrix)
    return result