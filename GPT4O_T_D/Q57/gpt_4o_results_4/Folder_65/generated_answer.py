import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrix_sum(start_row, start_col, end_row, end_col):
        submatrix = matrix[start_row:end_row + 1, start_col:end_col + 1]
        return (np.sum(submatrix), submatrix.tolist())
    rows, cols = matrix.shape
    result = []
    for start_row in range(rows):
        for start_col in range(cols):
            for end_row in range(start_row, rows):
                for end_col in range(start_col, cols):
                    sub_sum, submatrix = get_submatrix_sum(start_row, start_col, end_row, end_col)
                    if sub_sum == 78:
                        result.append(submatrix)
    return result