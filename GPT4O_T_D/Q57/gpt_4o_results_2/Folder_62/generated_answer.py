import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(matrix, start_row, start_col, end_row, end_col):
        return np.sum(matrix[start_row:end_row, start_col:end_col])
    rows, cols = matrix.shape
    submatrices = []
    for start_row in range(rows):
        for end_row in range(start_row + 1, rows + 1):
            for start_col in range(cols):
                for end_col in range(start_col + 1, cols + 1):
                    if submatrix_sum(matrix, start_row, start_col, end_row, end_col) == 394:
                        submatrices.append(matrix[start_row:end_row, start_col:end_col])
    return submatrices