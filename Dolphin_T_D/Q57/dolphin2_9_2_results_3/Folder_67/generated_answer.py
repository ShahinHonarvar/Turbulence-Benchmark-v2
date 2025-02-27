import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    row_num, col_num = matrix.shape
    for i in range(row_num):
        for j in range(col_num):
            for k in range(i, row_num):
                for l in range(j, col_num):
                    if i != k or j != l:
                        submatrix = matrix[i:k + 1, j:l + 1]
                        if np.sum(submatrix) == 40:
                            result.append(submatrix.tolist())
    return result