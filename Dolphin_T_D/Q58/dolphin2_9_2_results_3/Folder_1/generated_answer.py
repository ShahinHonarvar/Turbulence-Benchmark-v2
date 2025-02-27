import numpy as np

def submatrix_with_n_numbers(matrix):
    row_num = len(matrix)
    col_num = len(matrix[0])
    result = 0
    for left_col in range(col_num):
        for right_col in range(left_col + 1, col_num + 1):
            sub_matrix_sum = np.sum(matrix[:, left_col:right_col], axis=0)
            if sub_matrix_sum == 23:
                result += 1
    return result