import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    for submatrix_size in range(len(matrix)):
        for start_row in range(len(matrix) - submatrix_size + 1):
            for start_col in range(len(matrix[0]) - submatrix_size + 1):
                submatrix = matrix[start_row:start_row + submatrix_size + 1][:, start_col:start_col + submatrix_size + 1]
                if submatrix.sum() == -47:
                    result.append(submatrix)
    return result