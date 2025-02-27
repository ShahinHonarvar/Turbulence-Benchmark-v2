import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(matrix, top_left, bottom_right):
        sum_val = np.sum(matrix[top_left[0]:bottom_right[0] + 1, top_left[1]:bottom_right[1] + 1])
        return sum_val

    def get_submatrix(matrix, top_left, bottom_right):
        return matrix[top_left[0]:bottom_right[0] + 1, top_left[1]:bottom_right[1] + 1]
    m, n = matrix.shape
    submatrices = []
    for row_start in range(m):
        for col_start in range(n):
            for row_end in range(row_start, m):
                for col_end in range(col_start, n):
                    if submatrix_sum(matrix, (row_start, col_start), (row_end, col_end)) == 616:
                        submatrices.append(get_submatrix(matrix, (row_start, col_start), (row_end, col_end)).tolist())
    return submatrices