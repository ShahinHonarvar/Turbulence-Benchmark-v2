import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(mat, start_row, start_col, end_row, end_col):
        return np.sum(mat[start_row:end_row + 1, start_col:end_col + 1])
    rows, cols = matrix.shape
    result = []
    for start_row in range(rows):
        for start_col in range(cols):
            for end_row in range(start_row, rows):
                for end_col in range(start_col, cols):
                    if submatrix_sum(matrix, start_row, start_col, end_row, end_col) == -42:
                        submat = matrix[start_row:end_row + 1, start_col:end_col + 1]
                        result.append(submat.tolist())
    return result