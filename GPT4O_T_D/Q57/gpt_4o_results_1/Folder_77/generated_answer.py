import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices_ending_at(row, col):
        submatrices = []
        for start_row in range(row + 1):
            for start_col in range(col + 1):
                submatrix = matrix[start_row:row + 1, start_col:col + 1]
                submatrices.append(submatrix)
        return submatrices
    result = []
    rows, cols = matrix.shape
    for row in range(rows):
        for col in range(cols):
            submatrices = get_submatrices_ending_at(row, col)
            for submatrix in submatrices:
                if submatrix.sum() == -336:
                    result.append(submatrix.tolist())
    return result