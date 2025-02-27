import numpy as np

def submatrix_with_particular_sum(matrix):
    row_num, col_num = matrix.shape
    submatrices = []
    for i in range(row_num):
        for j in range(col_num):
            for end_i in range(i, row_num):
                for end_j in range(j, col_num):
                    submatrix_sum = np.sum(matrix[i:end_i + 1, j:end_j + 1])
                    if submatrix_sum == -4:
                        submatrices.append(matrix[i:end_i + 1, j:end_j + 1])
    return submatrices if submatrices else list()