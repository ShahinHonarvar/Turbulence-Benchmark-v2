import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrix_sum(matrix, start_row, end_row, start_col, end_col):
        submatrix = matrix[start_row:end_row, start_col:end_col]
        return (submatrix, np.sum(submatrix))
    result = []
    rows, cols = matrix.shape
    for start_row in range(rows):
        for start_col in range(cols):
            for end_row in range(start_row + 1, rows + 1):
                for end_col in range(start_col + 1, cols + 1):
                    submatrix, submatrix_sum = get_submatrix_sum(matrix, start_row, end_row, start_col, end_col)
                    if submatrix_sum == 38:
                        result.append(submatrix.tolist())
    return result