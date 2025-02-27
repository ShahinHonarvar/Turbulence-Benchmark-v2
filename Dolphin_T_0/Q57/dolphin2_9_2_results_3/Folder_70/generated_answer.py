import numpy as np

def submatrix_with_particular_sum(matrix):
    row_count, col_count = matrix.shape
    submatrices = []
    for i in range(row_count):
        for j in range(col_count):
            for k in range(i, row_count):
                for l in range(j, col_count):
                    sub_matrix = matrix[i:k + 1, j:l + 1]
                    if np.sum(sub_matrix) == 411:
                        submatrices.append(sub_matrix)
    return submatrices