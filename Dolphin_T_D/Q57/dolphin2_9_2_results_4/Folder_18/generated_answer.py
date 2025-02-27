import numpy as np

def submatrix_with_particular_sum(np_matrix):
    row_count, col_count = np_matrix.shape
    submatrix_set = []
    for i in range(row_count):
        for j in range(col_count):
            for k in range(i + 1, row_count):
                for l in range(j + 1, col_count):
                    if sum(sum(np_matrix[i:k + 1, j:l + 1])) == 616:
                        submatrix_set.append(np_matrix[i:k + 1, j:l + 1])
    return submatrix_set