import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(matrix):
        submatrices = []
        rows, cols = matrix.shape
        for row in range(rows):
            for col in range(cols):
                for sub_row in range(row + 1, rows + 1):
                    for sub_col in range(col + 1, cols + 1):
                        submatrices.append(matrix[row:sub_row, col:sub_col])
        return submatrices
    submatrices = get_submatrices(matrix)
    return [submatrix for submatrix in submatrices if np.sum(submatrix) == -20]