import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrix_sum(i1, j1, i2, j2):
        return np.sum(matrix[i1:i2 + 1, j1:j2 + 1])
    result = []
    rows, cols = matrix.shape
    for start_row in range(rows):
        for start_col in range(cols):
            for end_row in range(start_row, rows):
                for end_col in range(start_col, cols):
                    if get_submatrix_sum(start_row, start_col, end_row, end_col) == -65:
                        submatrix = matrix[start_row:end_row + 1, start_col:end_col + 1]
                        result.append(submatrix)
    return result