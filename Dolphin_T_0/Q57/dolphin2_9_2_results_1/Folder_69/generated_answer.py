import numpy as np

def submatrix_with_particular_sum(matrix):
    row_num, col_num = matrix.shape
    result = []
    for i in range(row_num):
        for j in range(col_num):
            for k in range(i + 1, row_num + 1):
                for l in range(j + 1, col_num + 1):
                    submatrix = np.array(matrix[i:k, j:l])
                    if np.sum(submatrix) == 752:
                        result.append(submatrix)
    return result