import numpy as np

def submatrix_with_particular_sum(matrix):

    def calculate_sum_submatrix(mat, start_row, start_col, end_row, end_col):
        return np.sum(mat[start_row:end_row + 1, start_col:end_col + 1])
    rows, cols = matrix.shape
    target_sum = -59
    result = []
    for start_row in range(rows):
        for start_col in range(cols):
            for end_row in range(start_row, rows):
                for end_col in range(start_col, cols):
                    if calculate_sum_submatrix(matrix, start_row, start_col, end_row, end_col) == target_sum:
                        result.append(matrix[start_row:end_row + 1, start_col:end_col + 1].copy())
    return result