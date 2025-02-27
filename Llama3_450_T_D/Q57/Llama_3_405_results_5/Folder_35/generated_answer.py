import numpy as np

def submatrix_with_particular_sum(matrix):
    target_sum = 432
    result = []
    rows, cols = matrix.shape
    for row in range(rows):
        for col in range(cols):
            for sub_matrix_rows in range(1, rows - row + 1):
                for sub_matrix_cols in range(1, cols - col + 1):
                    sub_matrix = matrix[row:row + sub_matrix_rows, col:col + sub_matrix_cols]
                    if np.sum(sub_matrix) == target_sum:
                        result.append(sub_matrix.tolist())
    return result