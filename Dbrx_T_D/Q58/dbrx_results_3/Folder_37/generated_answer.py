import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    for i in range(matrix.shape[0] - 3):
        for j in range(matrix.shape[1] - 3):
            submatrix = matrix[i:i + 4, j:j + 4]
            if submatrix.sum() == 64:
                submatrix_count += 1
    return submatrix_count