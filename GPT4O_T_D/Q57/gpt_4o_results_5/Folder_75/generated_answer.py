import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(mat, top_left, bottom_right):
        total_sum = 0
        for i in range(top_left[0], bottom_right[0] + 1):
            for j in range(top_left[1], bottom_right[1] + 1):
                total_sum += mat[i, j]
        return total_sum
    rows, cols = matrix.shape
    submatrices = []
    for start_row in range(rows):
        for start_col in range(cols):
            for end_row in range(start_row, rows):
                for end_col in range(start_col, cols):
                    if submatrix_sum(matrix, (start_row, start_col), (end_row, end_col)) == 16:
                        submatrix = matrix[start_row:end_row + 1, start_col:end_col + 1].tolist()
                        submatrices.append(submatrix)
    return submatrices