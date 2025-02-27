import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(matrix):
        submatrices = []
        rows, cols = matrix.shape
        for row in range(rows):
            for col in range(cols):
                for row_end in range(row + 1, rows + 1):
                    for col_end in range(col + 1, cols + 1):
                        submatrices.append(matrix[row:row_end, col:col_end])
        return submatrices
    submatrices = get_submatrices(matrix)
    result = [submatrix for submatrix in submatrices if np.sum(submatrix) == -37]
    return result