import numpy as np

def submatrix_with_particular_sum(matrix):

    def generate_submatrices(r1, c1, r2, c2):
        return matrix[r1:r2, c1:c2]
    rows, cols = matrix.shape
    result = []
    for start_row in range(rows):
        for end_row in range(start_row + 1, rows + 1):
            for start_col in range(cols):
                for end_col in range(start_col + 1, cols + 1):
                    submatrix = generate_submatrices(start_row, start_col, end_row, end_col)
                    if np.sum(submatrix) == 901:
                        result.append(submatrix)
    return result