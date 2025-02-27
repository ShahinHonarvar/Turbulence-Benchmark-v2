import numpy as np

def submatrix_with_particular_sum(matrix):

    def extract_submatrix(matrix, row_start, row_end, col_start, col_end):
        return matrix[row_start:row_end + 1, col_start:col_end + 1]
    rows, cols = matrix.shape
    submatrices_with_sum_negative_three = []
    for row_start in range(rows):
        for col_start in range(cols):
            for row_end in range(row_start, rows):
                for col_end in range(col_start, cols):
                    submatrix = extract_submatrix(matrix, row_start, row_end, col_start, col_end)
                    if np.sum(submatrix) == -3:
                        submatrices_with_sum_negative_three.append(submatrix)
    return submatrices_with_sum_negative_three