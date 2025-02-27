import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices_of_size(i, j, rows, cols):
        submatrices = []
        for ii in range(matrix.shape[0] - i + 1):
            for jj in range(matrix.shape[1] - j + 1):
                submatrix = matrix[ii:ii + i, jj:jj + j]
                if np.sum(submatrix) == 64:
                    submatrices.append(submatrix)
        return submatrices
    all_submatrices = []
    for rows in range(1, matrix.shape[0] + 1):
        for cols in range(1, matrix.shape[1] + 1):
            all_submatrices.extend(get_submatrices_of_size(rows, cols, rows, cols))
    return all_submatrices