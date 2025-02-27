import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrix_sum(submat):
        return np.sum(submat)

    def find_submatrices(matrix):
        rows, cols = matrix.shape
        submatrices = []
        for row_start in range(rows):
            for row_end in range(row_start, rows):
                for col_start in range(cols):
                    for col_end in range(col_start, cols):
                        submat = matrix[row_start:row_end + 1, col_start:col_end + 1]
                        if get_submatrix_sum(submat) == -779:
                            submatrices.append(submat)
        return submatrices
    return find_submatrices(matrix)