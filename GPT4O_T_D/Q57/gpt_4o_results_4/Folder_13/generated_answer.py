import numpy as np

def submatrix_with_particular_sum(matrix):

    def check_submatrix_sum(mat, target, start_row, start_col, end_row, end_col):
        sub_sum = np.sum(mat[start_row:end_row + 1, start_col:end_col + 1])
        return sub_sum == target
    result = []
    n_rows, n_cols = matrix.shape
    for start_row in range(n_rows):
        for start_col in range(n_cols):
            for end_row in range(start_row, n_rows):
                for end_col in range(start_col, n_cols):
                    if check_submatrix_sum(matrix, 382, start_row, start_col, end_row, end_col):
                        submatrix = matrix[start_row:end_row + 1, start_col:end_col + 1].tolist()
                        result.append(submatrix)
    return result