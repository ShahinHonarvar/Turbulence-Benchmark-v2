import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    target_sum = -261
    result = []
    for start_row in range(m):
        for start_col in range(n):
            for end_row in range(start_row, m):
                for end_col in range(start_col, n):
                    submatrix = matrix[start_row:end_row + 1, start_col:end_col + 1]
                    if np.sum(submatrix) == target_sum:
                        result.append(submatrix.tolist())
    return result