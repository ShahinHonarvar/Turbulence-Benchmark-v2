import numpy as np

def submatrix_with_particular_sum(matrix):

    def all_submatrices(mat):
        submatrices = []
        rows, cols = mat.shape
        for row_start in range(rows):
            for row_end in range(row_start, rows):
                for col_start in range(cols):
                    for col_end in range(col_start, cols):
                        submatrix = mat[row_start:row_end + 1, col_start:col_end + 1]
                        submatrices.append(submatrix)
        return submatrices
    specific_sum = 77
    submatrices = all_submatrices(matrix)
    result = []
    for submatrix in submatrices:
        if np.sum(submatrix) == specific_sum:
            result.append(submatrix.tolist())
    return result