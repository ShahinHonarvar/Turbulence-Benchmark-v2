import numpy as np

def submatrix_with_n_numbers(matrix):
    row_num, col_num = matrix.shape
    count = 0
    submatrix_size = 11
    for i in range(row_num - submatrix_size + 1):
        for j in range(col_num - submatrix_size + 1):
            if np.count_nonzero(matrix[i:i + submatrix_size, j:j + submatrix_size]) == 166:
                count += 1
    return count