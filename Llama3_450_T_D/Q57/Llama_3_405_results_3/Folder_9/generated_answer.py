import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    num_rows, num_cols = matrix.shape
    for row_start in range(num_rows):
        for row_end in range(row_start + 1, num_rows + 1):
            for col_start in range(num_cols):
                for col_end in range(col_start + 1, num_cols + 1):
                    submatrix = matrix[row_start:row_end, col_start:col_end]
                    if np.sum(submatrix) == -86:
                        result.append(submatrix.tolist())
    return result