import numpy as np

def submatrix_with_n_numbers(matrix):
    row_num, col_num = matrix.shape
    count = 0
    for i in range(row_num):
        for j in range(col_num):
            if matrix[i:i + 5, j:j + 5].size == 25:
                count += 1
    if count:
        return count
    else:
        return 0