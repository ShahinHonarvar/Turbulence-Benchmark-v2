import numpy as np

def submatrix_with_n_numbers(matrix):
    shape = matrix.shape
    submatrix_count = 0
    for i in range(shape[0]):
        for j in range(shape[1]):
            for k in range(i, shape[0]):
                for l in range(j, shape[1]):
                    if len(matrix[i:k + 1, j:l + 1].flatten()) == 39:
                        submatrix_count += 1
    return submatrix_count if submatrix_count else 0