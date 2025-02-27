import numpy as np

def submatrix_with_n_numbers(matrix):
    row_count = matrix.shape[0]
    col_count = matrix.shape[1]
    target_count = 80
    count = 0
    for row in range(row_count):
        for col in range(col_count):
            for sub_row_count in range(1, row_count - row + 1):
                for sub_col_count in range(1, col_count - col + 1):
                    if sub_row_count * sub_col_count == target_count:
                        submatrix = matrix[row:row + sub_row_count, col:col + sub_col_count]
                        if np.size(submatrix) == target_count:
                            count += 1
    return count