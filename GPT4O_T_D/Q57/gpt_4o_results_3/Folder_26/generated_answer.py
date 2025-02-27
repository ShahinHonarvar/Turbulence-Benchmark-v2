import numpy as np

def submatrix_with_particular_sum(matrix):

    def sum_submatrix(submatrix):
        return np.sum(submatrix)

    def generate_submatrices(matrix):
        rows, cols = matrix.shape
        for start_row in range(rows):
            for start_col in range(cols):
                for end_row in range(start_row, rows):
                    for end_col in range(start_col, cols):
                        yield matrix[start_row:end_row + 1, start_col:end_col + 1]
    submatrices = []
    for submatrix in generate_submatrices(matrix):
        if sum_submatrix(submatrix) == 997:
            submatrices.append(submatrix)
    return submatrices