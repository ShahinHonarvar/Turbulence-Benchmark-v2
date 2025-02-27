import numpy as np

def submatrix_with_particular_sum(matrix):
    row_num, col_num = matrix.shape
    submatrices = []
    for i in range(row_num):
        for j in range(col_num):
            for row_size in range(i + 1, row_num + 1):
                for col_size in range(j + 1, col_num + 1):
                    submatrix_sum = np.sum(matrix[i:row_size, j:col_size])
                    if submatrix_sum == 901:
                        submatrices.append(matrix[i:row_size, j:col_size])
    return submatrices