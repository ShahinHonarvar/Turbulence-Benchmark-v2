import numpy as np

def submatrix_with_n_numbers(matrix):
    row_num, col_num = matrix.shape
    counter = 0
    for i in range(row_num):
        for j in range(col_num):
            if matrix[i][j] == 1:
                counter += 1
    return counter