import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrix_sum(matrix, row_start, row_end, col_start, col_end):
        return np.sum(matrix[row_start:row_end + 1, col_start:col_end + 1])
    num_rows, num_cols = matrix.shape
    result = []
    for row_start in range(num_rows):
        for row_end in range(row_start, num_rows):
            for col_start in range(num_cols):
                for col_end in range(col_start, num_cols):
                    if get_submatrix_sum(matrix, row_start, row_end, col_start, col_end) == -452:
                        result.append(matrix[row_start:row_end + 1, col_start:col_end + 1].tolist())
    return result