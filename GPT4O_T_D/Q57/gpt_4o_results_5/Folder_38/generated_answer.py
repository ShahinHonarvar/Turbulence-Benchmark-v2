import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrix_sum(matrix, row_start, row_end, col_start, col_end):
        submatrix = matrix[row_start:row_end + 1, col_start:col_end + 1]
        return (np.sum(submatrix), submatrix.tolist())
    rows, cols = matrix.shape
    result = []
    for row_start in range(rows):
        for row_end in range(row_start, rows):
            for col_start in range(cols):
                for col_end in range(col_start, cols):
                    submatrix_sum, submatrix = get_submatrix_sum(matrix, row_start, row_end, col_start, col_end)
                    if submatrix_sum == 34:
                        result.append(submatrix)
    return result