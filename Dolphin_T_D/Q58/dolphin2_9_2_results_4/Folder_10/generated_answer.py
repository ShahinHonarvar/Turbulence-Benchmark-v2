import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    shape = matrix.shape
    for i in range(shape[0]):
        for j in range(shape[1]):
            for k in range(i, shape[0]):
                for l in range(j, shape[1]):
                    if len(matrix[i:k + 1, j:l + 1].flatten()) == 56:
                        count += 1
    return count