import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrix_sum(matrix, top_left, bottom_right):
        submatrix = matrix[top_left[0]:bottom_right[0] + 1, top_left[1]:bottom_right[1] + 1]
        return np.sum(submatrix)
    rows, cols = matrix.shape
    result = []
    for row_start in range(rows):
        for col_start in range(cols):
            for row_end in range(row_start, rows):
                for col_end in range(col_start, cols):
                    submatrix_sum = get_submatrix_sum(matrix, (row_start, col_start), (row_end, col_end))
                    if submatrix_sum == 126:
                        submatrix = matrix[row_start:row_end + 1, col_start:col_end + 1].tolist()
                        result.append(submatrix)
    return result