import numpy as np

def submatrix_with_particular_sum(matrix):

    def calculate_sum(submatrix):
        return np.sum(submatrix)
    num_rows, num_cols = matrix.shape
    submatrices_with_sum_84 = []
    for row_start in range(num_rows):
        for row_end in range(row_start, num_rows):
            for col_start in range(num_cols):
                for col_end in range(col_start, num_cols):
                    submatrix = matrix[row_start:row_end + 1, col_start:col_end + 1]
                    if calculate_sum(submatrix) == 84:
                        submatrices_with_sum_84.append(submatrix.tolist())
    return submatrices_with_sum_84