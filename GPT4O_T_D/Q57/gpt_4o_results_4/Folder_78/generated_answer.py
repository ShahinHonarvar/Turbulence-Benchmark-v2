import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrices(matrix):
        r, c = matrix.shape
        for start_row in range(r):
            for start_col in range(c):
                for end_row in range(start_row + 1, r + 1):
                    for end_col in range(start_col + 1, c + 1):
                        yield matrix[start_row:end_row, start_col:end_col]
    result = []
    for submatrix in submatrices(matrix):
        if np.sum(submatrix) == 17:
            result.append(submatrix)
    return result