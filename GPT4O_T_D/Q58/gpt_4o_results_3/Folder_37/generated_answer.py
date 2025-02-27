import numpy as np

def submatrix_with_n_numbers(matrix):
    row_count, col_count = matrix.shape
    submatrix_count = 0
    for i in range(row_count):
        for j in range(col_count):
            for k in range(i + 1, row_count + 1):
                for l in range(j + 1, col_count + 1):
                    submatrix = matrix[i:k, j:l]
                    if submatrix.size == 64:
                        submatrix_count += 1
    return submatrix_count