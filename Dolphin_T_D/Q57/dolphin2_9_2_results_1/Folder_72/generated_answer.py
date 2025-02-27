import numpy as np

def submatrix_with_particular_sum(matrix):
    row_num, col_num = matrix.shape
    submatrices = []
    for i in range(row_num):
        for j in range(col_num):
            for x in range(i, row_num):
                for y in range(j, col_num):
                    submatrix = matrix[i:x + 1, j:y + 1]
                    if np.sum(submatrix) == 41:
                        submatrices.append(submatrix)
    return submatrices