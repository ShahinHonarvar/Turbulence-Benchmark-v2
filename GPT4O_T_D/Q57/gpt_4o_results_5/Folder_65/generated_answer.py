import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrix_sum(top_left, bottom_right):
        total_sum = 0
        for i in range(top_left[0], bottom_right[0] + 1):
            for j in range(top_left[1], bottom_right[1] + 1):
                total_sum += matrix[i][j]
        return total_sum
    rows, cols = matrix.shape
    found_submatrices = []
    for row_start in range(rows):
        for col_start in range(cols):
            for row_end in range(row_start, rows):
                for col_end in range(col_start, cols):
                    if get_submatrix_sum((row_start, col_start), (row_end, col_end)) == 78:
                        submatrix = matrix[row_start:row_end + 1, col_start:col_end + 1]
                        found_submatrices.append(submatrix.tolist())
    return found_submatrices