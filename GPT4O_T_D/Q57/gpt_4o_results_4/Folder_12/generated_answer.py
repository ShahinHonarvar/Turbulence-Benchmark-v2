import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrix_sum(x1, y1, x2, y2):
        return np.sum(matrix[x1:x2 + 1, y1:y2 + 1])
    num_rows, num_cols = matrix.shape
    submatrices = []
    for row_start in range(num_rows):
        for row_end in range(row_start, num_rows):
            for col_start in range(num_cols):
                for col_end in range(col_start, num_cols):
                    if get_submatrix_sum(row_start, col_start, row_end, col_end) == -83:
                        submatrix = matrix[row_start:row_end + 1, col_start:col_end + 1].tolist()
                        submatrices.append(submatrix)
    return submatrices