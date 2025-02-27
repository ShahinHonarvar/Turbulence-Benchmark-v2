import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(matrix):
        rows, cols = matrix.shape
        for row_start in range(rows):
            for row_end in range(row_start, rows):
                for col_start in range(cols):
                    for col_end in range(col_start, cols):
                        yield matrix[row_start:row_end + 1, col_start:col_end + 1]

    def sum_matrix(submatrix):
        return np.sum(submatrix)
    submatrices = get_submatrices(matrix)
    matching_submatrices = []
    for submatrix in submatrices:
        if sum_matrix(submatrix) == 862:
            matching_submatrices.append(submatrix)
    return matching_submatrices