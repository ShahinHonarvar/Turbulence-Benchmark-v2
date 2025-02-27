import numpy as np

def submatrix_with_particular_sum(matrix):

    def sum_of_submatrix(matrix, row_start, row_end, col_start, col_end):
        return np.sum(matrix[row_start:row_end + 1, col_start:col_end + 1])
    result = []
    rows, cols = matrix.shape
    for row_start in range(rows):
        for row_end in range(row_start, rows):
            for col_start in range(cols):
                for col_end in range(col_start, cols):
                    if sum_of_submatrix(matrix, row_start, row_end, col_start, col_end) == 15:
                        submatrix = matrix[row_start:row_end + 1, col_start:col_end + 1]
                        result.append(submatrix.tolist())
    return result