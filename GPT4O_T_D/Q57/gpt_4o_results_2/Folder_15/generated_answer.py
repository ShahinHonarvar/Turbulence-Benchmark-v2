import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(matrix, start_row, start_col):
        submatrices = []
        for end_row in range(start_row, matrix.shape[0]):
            for end_col in range(start_col, matrix.shape[1]):
                submatrix = matrix[start_row:end_row + 1, start_col:end_col + 1]
                submatrices.append(submatrix)
        return submatrices
    result = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            submatrices = get_submatrices(matrix, i, j)
            for submatrix in submatrices:
                if np.sum(submatrix) == -9:
                    result.append(submatrix)
    return result