import numpy as np

def submatrix_with_particular_sum(matrix):
    row_num, col_num = matrix.shape
    submatrices = []
    for top_row in range(row_num):
        for bottom_row in range(top_row, row_num):
            for left_col in range(col_num):
                for right_col in range(left_col, col_num):
                    submatrix = np.array(matrix[top_row:bottom_row + 1, left_col:right_col + 1])
                    if np.sum(submatrix) == 416:
                        submatrices.append(submatrix)
    return submatrices