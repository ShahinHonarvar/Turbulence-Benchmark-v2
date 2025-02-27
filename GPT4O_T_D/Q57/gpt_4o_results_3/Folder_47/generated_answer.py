import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices_with_sum(target_sum, rows, cols):
        result = []
        for row_start in range(rows):
            for col_start in range(cols):
                for row_end in range(row_start, rows):
                    for col_end in range(col_start, cols):
                        submatrix = matrix[row_start:row_end + 1, col_start:col_end + 1]
                        if np.sum(submatrix) == target_sum:
                            result.append(submatrix)
        return result
    rows, cols = matrix.shape
    return get_submatrices_with_sum(27, rows, cols)