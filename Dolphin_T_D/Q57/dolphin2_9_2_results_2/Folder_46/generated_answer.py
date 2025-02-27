import numpy as np

def submatrix_with_particular_sum(matrix):
    row_num, col_num = matrix.shape
    result = []
    for r1 in range(row_num):
        for r2 in range(r1, row_num):
            for c1 in range(col_num):
                for c2 in range(c1, col_num):
                    submatrix_sum = np.sum(matrix[r1:r2 + 1, c1:c2 + 1])
                    if submatrix_sum == 416:
                        result.append(matrix[r1:r2 + 1, c1:c2 + 1])
    return result