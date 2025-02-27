import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(matrix):
        submatrices = []
        for row_start in range(matrix.shape[0]):
            for row_end in range(row_start + 1, matrix.shape[0] + 1):
                for col_start in range(matrix.shape[1]):
                    for col_end in range(col_start + 1, matrix.shape[1] + 1):
                        submatrices.append(matrix[row_start:row_end, col_start:col_end])
        return submatrices
    submatrices = get_submatrices(matrix)
    result = [submatrix for submatrix in submatrices if np.sum(submatrix) == -4]
    return result