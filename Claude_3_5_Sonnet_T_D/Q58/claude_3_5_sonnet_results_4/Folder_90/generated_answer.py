import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    target_count = 176
    submatrix_count = 0
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.size == target_count:
                        submatrix_count += 1
    return submatrix_count