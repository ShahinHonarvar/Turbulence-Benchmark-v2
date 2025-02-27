import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(matrix, r, c):
        submatrices = []
        rows, cols = matrix.shape
        for start_row in range(rows):
            for start_col in range(cols):
                for end_row in range(start_row + 1, rows + 1):
                    for end_col in range(start_col + 1, cols + 1):
                        submatrices.append(matrix[start_row:end_row, start_col:end_col])
        return submatrices
    submatrices = get_submatrices(matrix, matrix.shape[0], matrix.shape[1])
    result = [submatrix.tolist() for submatrix in submatrices if np.sum(submatrix) == 54]
    return result