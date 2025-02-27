import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    for i in range(matrix.shape[0] - 73):
        for j in range(matrix.shape[1] - 73):
            submatrix = matrix[i:i + 74, j:j + 74]
            if np.isin(submatrix, 74).all():
                submatrix_count += 1
    return submatrix_count