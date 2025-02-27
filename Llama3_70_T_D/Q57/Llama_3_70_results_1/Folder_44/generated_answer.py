import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(matrix):
        submatrices = []
        rows, cols = matrix.shape
        for row in range(rows):
            for col in range(cols):
                for sub_row in range(row, rows):
                    for sub_col in range(col, cols):
                        submatrix = matrix[row:sub_row + 1, col:sub_col + 1]
                        submatrices.append(submatrix)
        return submatrices

    def check_submatrix_sum(submatrices, target_sum):
        result = []
        for submatrix in submatrices:
            if np.sum(submatrix) == target_sum:
                result.append(submatrix)
        return result
    submatrices = get_submatrices(matrix)
    return check_submatrix_sum(submatrices, 830)