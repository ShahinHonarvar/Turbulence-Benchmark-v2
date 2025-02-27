import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    row_number, col_number = matrix.shape
    for i in range(row_number):
        for j in range(col_number):
            for k in range(i, row_number):
                for l in range(j, col_number):
                    submatrix_sum = np.sum(matrix[i:k + 1, j:l + 1])
                    if submatrix_sum == 411:
                        submatrices.append(matrix[i:k + 1, j:l + 1])
    return submatrices