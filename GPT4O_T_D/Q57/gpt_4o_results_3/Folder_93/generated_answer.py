import numpy as np

def submatrix_with_particular_sum(matrix):

    def sum_submatrix(mat, top_left, bottom_right):
        row_start, col_start = top_left
        row_end, col_end = bottom_right
        return np.sum(mat[row_start:row_end, col_start:col_end])
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        return []
    rows, cols = matrix.shape
    target_sum = -65
    result = []
    for row_start in range(rows):
        for row_end in range(row_start + 1, rows + 1):
            for col_start in range(cols):
                for col_end in range(col_start + 1, cols + 1):
                    submatrix_sum = sum_submatrix(matrix, (row_start, col_start), (row_end, col_end))
                    if submatrix_sum == target_sum:
                        submatrix = matrix[row_start:row_end, col_start:col_end]
                        result.append(submatrix.tolist())
    return result