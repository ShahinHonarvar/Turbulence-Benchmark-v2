import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(matrix):
        row_len, col_len = matrix.shape
        for row_start in range(row_len):
            for row_end in range(row_start, row_len):
                for col_start in range(col_len):
                    for col_end in range(col_start, col_len):
                        yield matrix[row_start:row_end + 1, col_start:col_end + 1]
    submatrices = list(get_submatrices(matrix))
    result = [submat for submat in submatrices if np.sum(submat) == -128]
    return result