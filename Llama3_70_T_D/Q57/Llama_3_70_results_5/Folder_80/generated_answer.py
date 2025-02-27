import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for row_start in range(rows):
        for row_end in range(row_start, rows):
            for col_start in range(cols):
                for col_end in range(col_start, cols):
                    submatrix_sum = np.sum(matrix[row_start:row_end + 1, col_start:col_end + 1])
                    if submatrix_sum == 245:
                        result.append(matrix[row_start:row_end + 1, col_start:col_end + 1].tolist())
    return result