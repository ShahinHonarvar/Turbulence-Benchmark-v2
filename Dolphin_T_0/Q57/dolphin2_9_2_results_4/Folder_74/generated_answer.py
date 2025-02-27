import numpy as np

def submatrix_with_particular_sum(matrix):
    row_num, col_num = matrix.shape
    submatrices = []
    for i in range(row_num):
        for j in range(col_num):
            for x in range(i + 1, row_num + 1):
                for y in range(j + 1, col_num + 1):
                    submatrix_sum = np.sum(matrix[i:x, j:y])
                    if submatrix_sum == 88:
                        submatrices.append(matrix[i:x, j:y])
    return submatrices