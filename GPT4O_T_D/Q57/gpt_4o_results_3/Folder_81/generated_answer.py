import numpy as np

def submatrix_with_particular_sum(matrix):

    def calculate_sum(matrix, row_start, row_end, col_start, col_end):
        return np.sum(matrix[row_start:row_end + 1, col_start:col_end + 1])
    rows, cols = matrix.shape
    result = []
    for row_start in range(rows):
        for row_end in range(row_start, rows):
            for col_start in range(cols):
                for col_end in range(col_start, cols):
                    if calculate_sum(matrix, row_start, row_end, col_start, col_end) == -90:
                        submatrix = matrix[row_start:row_end + 1, col_start:col_end + 1]
                        result.append(submatrix.tolist())
    return result