import numpy as np

def submatrix_with_particular_sum(matrix):

    def sum_submatrix(start_row, start_col, end_row, end_col):
        return np.sum(matrix[start_row:end_row + 1, start_col:end_col + 1])
    result = []
    n_rows, n_cols = matrix.shape
    for start_row in range(n_rows):
        for end_row in range(start_row, n_rows):
            for start_col in range(n_cols):
                for end_col in range(start_col, n_cols):
                    if sum_submatrix(start_row, start_col, end_row, end_col) == -137:
                        submatrix = matrix[start_row:end_row + 1, start_col:end_col + 1]
                        result.append(submatrix.tolist())
    return result