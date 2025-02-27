import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(matrix):
        rows, cols = matrix.shape
        for start_row in range(rows):
            for start_col in range(cols):
                for end_row in range(start_row, rows):
                    for end_col in range(start_col, cols):
                        yield matrix[start_row:end_row + 1, start_col:end_col + 1]
    result = []
    for submatrix in get_submatrices(matrix):
        if np.sum(submatrix) == -779:
            result.append(submatrix)
    return result