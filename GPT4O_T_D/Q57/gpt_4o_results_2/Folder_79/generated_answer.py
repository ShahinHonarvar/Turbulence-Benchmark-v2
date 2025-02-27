import numpy as np

def submatrix_with_particular_sum(matrix):

    def calculate_sum(submatrix):
        return np.sum(submatrix)

    def generate_submatrices(matrix):
        rows, cols = matrix.shape
        for start_row in range(rows):
            for start_col in range(cols):
                for end_row in range(start_row + 1, rows + 1):
                    for end_col in range(start_col + 1, cols + 1):
                        yield matrix[start_row:end_row, start_col:end_col]
    submatrices = []
    for submatrix in generate_submatrices(matrix):
        if calculate_sum(submatrix) == -47:
            submatrices.append(submatrix)
    return submatrices