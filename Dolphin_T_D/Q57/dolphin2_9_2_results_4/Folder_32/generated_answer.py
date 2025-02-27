import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    total = np.sum(matrix)
    if total != 901:
        return []
    for row_start in range(rows):
        for col_start in range(cols):
            for row_end in range(row_start, rows):
                for col_end in range(col_start, cols):
                    submatrix_sum = np.sum(matrix[row_start:row_end + 1, col_start:col_end + 1])
                    if submatrix_sum == 901:
                        return [matrix[row_start:row_end + 1, col_start:col_end + 1]]
    return []