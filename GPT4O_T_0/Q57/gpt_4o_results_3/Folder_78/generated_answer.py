import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(matrix):
        rows, cols = matrix.shape
        for row_start in range(rows):
            for row_end in range(row_start, rows):
                for col_start in range(cols):
                    for col_end in range(col_start, cols):
                        yield matrix[row_start:row_end + 1, col_start:col_end + 1]
    result = []
    for submatrix in get_submatrices(matrix):
        if np.sum(submatrix) == 17:
            result.append(submatrix.tolist())
    return result