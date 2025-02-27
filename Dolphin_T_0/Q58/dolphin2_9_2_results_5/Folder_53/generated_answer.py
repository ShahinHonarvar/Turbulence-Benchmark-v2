import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    h, w = matrix.shape
    row_sum = np.sum(matrix, 1)
    for i in range(h):
        for j in range(i + 1, h):
            submatrix = np.sum(matrix[i:j + 1], 0)
            if all((x == 24 for x in submatrix)):
                submatrix_count += 1
    return submatrix_count