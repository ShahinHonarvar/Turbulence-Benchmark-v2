import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    num_rows, num_cols = matrix.shape
    for row_start in range(num_rows):
        for row_end in range(row_start, num_rows):
            for col_start in range(num_cols):
                for col_end in range(col_start, num_cols):
                    submatrix = matrix[row_start:row_end + 1, col_start:col_end + 1]
                    if np.sum(submatrix) == -59:
                        result.append(submatrix)
    return result