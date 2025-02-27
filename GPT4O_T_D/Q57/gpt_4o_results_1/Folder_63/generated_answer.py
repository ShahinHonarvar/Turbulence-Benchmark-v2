import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(submatrix):
        return np.sum(submatrix)

    def get_all_submatrices(matrix):
        rows, cols = matrix.shape
        for start_row in range(rows):
            for start_col in range(cols):
                for end_row in range(start_row, rows):
                    for end_col in range(start_col, cols):
                        yield matrix[start_row:end_row + 1, start_col:end_col + 1]
    all_submatrices = get_all_submatrices(matrix)
    result = [sm for sm in all_submatrices if submatrix_sum(sm) == 64]
    return result