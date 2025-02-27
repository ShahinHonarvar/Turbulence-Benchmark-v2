import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(submatrix):
        return np.sum(submatrix)

    def extract_submatrix(matrix, start_row, start_col, end_row, end_col):
        return matrix[start_row:end_row + 1, start_col:end_col + 1]
    rows, cols = matrix.shape
    submatrices = []
    for start_row in range(rows):
        for start_col in range(cols):
            for end_row in range(start_row, rows):
                for end_col in range(start_col, cols):
                    submatrix = extract_submatrix(matrix, start_row, start_col, end_row, end_col)
                    if submatrix_sum(submatrix) == -863:
                        submatrices.append(submatrix)
    return submatrices