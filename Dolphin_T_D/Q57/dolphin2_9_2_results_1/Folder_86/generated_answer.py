import numpy as np

def submatrix_with_particular_sum(matrix):
    row_num, col_num = matrix.shape
    result = []
    for i in range(row_num):
        for j in range(col_num):
            for a in range(i, row_num):
                for b in range(j, col_num):
                    if np.sum(matrix[i:a + 1, j:b + 1]) == -394:
                        result.append(matrix[i:a + 1, j:b + 1])
    return result