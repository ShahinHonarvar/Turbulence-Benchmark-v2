import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(submatrix):
        return np.sum(submatrix)

    def find_submatrices(matrix, sum_value, row_range, col_range):
        submatrices = []
        for row_start in range(row_range[0], row_range[1]):
            for row_end in range(row_start, row_range[2]):
                for col_start in range(col_range[0], col_range[1]):
                    for col_end in range(col_start, col_range[2]):
                        submatrix = matrix[row_start:row_end + 1, col_start:col_end + 1]
                        if submatrix_sum(submatrix) == sum_value:
                            submatrices.append(submatrix)
        return submatrices
    rows, cols = matrix.shape
    return find_submatrices(matrix, -394, (0, rows, 1), (0, cols, 1))