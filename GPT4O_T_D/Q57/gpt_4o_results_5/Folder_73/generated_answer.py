import numpy as np

def submatrix_with_particular_sum(matrix):
    target_sum = 93
    rows, cols = matrix.shape
    result = []

    def submatrix_sum(r1, c1, r2, c2):
        return np.sum(matrix[r1:r2 + 1, c1:c2 + 1])
    for start_row in range(rows):
        for start_col in range(cols):
            for end_row in range(start_row, rows):
                for end_col in range(start_col, cols):
                    if submatrix_sum(start_row, start_col, end_row, end_col) == target_sum:
                        result.append(matrix[start_row:end_row + 1, start_col:end_col + 1].tolist())
    return result