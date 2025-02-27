import numpy as np

def submatrix_with_particular_sum(matrix):
    while True:
        submatrices = []
        shape = matrix.shape
        row_num = shape[0]
        col_num = shape[1]
        for i in range(row_num):
            for j in range(col_num):
                row = []
                for x in range(i, row_num):
                    for y in range(j, col_num):
                        row.append(matrix[x, y])
                submatrices.append(row)
        new_submatrices = [sub for sub in submatrices if sum(sub) == -97]
        if len(new_submatrices) > 0:
            return new_submatrices
        else:
            return []