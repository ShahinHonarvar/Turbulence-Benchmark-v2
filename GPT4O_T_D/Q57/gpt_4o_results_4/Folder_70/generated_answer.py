import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(m):
        rows, cols = m.shape
        submatrices = []
        for start_row in range(rows):
            for start_col in range(cols):
                for end_row in range(start_row, rows):
                    for end_col in range(start_col, cols):
                        submatrix = m[start_row:end_row + 1, start_col:end_col + 1]
                        submatrices.append(submatrix)
        return submatrices

    def submatrix_sum(submatrix):
        return np.sum(submatrix)
    submatrices = get_submatrices(matrix)
    result = [sub for sub in submatrices if submatrix_sum(sub) == 411]
    return result