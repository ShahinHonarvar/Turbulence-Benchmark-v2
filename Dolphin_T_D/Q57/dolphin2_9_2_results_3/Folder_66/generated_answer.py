import numpy as np

def submatrix_with_particular_sum(matrix):
    output = []
    row_num, col_num = matrix.shape
    for x in range(row_num):
        for y in range(col_num):
            for x_new in range(x, row_num):
                for y_new in range(y, col_num):
                    if sum(matrix[x:x_new, y:y_new]) == 99:
                        output.append(matrix[x:x_new, y:y_new])
    return output