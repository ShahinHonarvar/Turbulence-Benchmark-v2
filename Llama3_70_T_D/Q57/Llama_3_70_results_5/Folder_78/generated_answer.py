import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(matrix):
        submatrices = []
        rows, cols = matrix.shape
        for row in range(rows):
            for col in range(cols):
                for sub_row in range(row, rows):
                    for sub_col in range(col, cols):
                        submatrices.append(matrix[row:sub_row + 1, col:sub_col + 1])
        return submatrices

    def get_sum(submatrix):
        return np.sum(submatrix)
    submatrices = get_submatrices(matrix)
    result = [submatrix for submatrix in submatrices if get_sum(submatrix) == 17]
    return result