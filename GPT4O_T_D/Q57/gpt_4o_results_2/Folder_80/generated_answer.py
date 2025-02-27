import numpy as np

def submatrix_with_particular_sum(matrix):
    num_rows, num_cols = matrix.shape
    result = []
    for start_row in range(num_rows):
        for start_col in range(num_cols):
            for end_row in range(start_row, num_rows):
                for end_col in range(start_col, num_cols):
                    submatrix = matrix[start_row:end_row + 1, start_col:end_col + 1]
                    if submatrix.sum() == 245:
                        result.append(submatrix.tolist())
    return result