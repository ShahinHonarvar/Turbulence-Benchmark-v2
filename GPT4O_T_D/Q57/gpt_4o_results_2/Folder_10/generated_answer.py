import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(m, n):
        for row_start in range(row_count):
            for row_end in range(row_start + 1, row_count + 1):
                for col_start in range(col_count):
                    for col_end in range(col_start + 1, col_count + 1):
                        yield m[row_start:row_end, col_start:col_end]
    row_count, col_count = matrix.shape
    submatrices = list(get_submatrices(matrix, 56))
    return [submatrix.tolist() for submatrix in submatrices if np.sum(submatrix) == 56]