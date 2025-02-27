import numpy as np

def submatrix_with_n_numbers(matrix):
    n = matrix.size
    row_num, col_num = matrix.shape
    count = 0
    for i in range(row_num):
        for j in range(col_num):
            for k in range(i, row_num):
                for l in range(j, col_num):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.size == 176:
                        count += 1
    return count