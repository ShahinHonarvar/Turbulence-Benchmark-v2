import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    for i in range(matrix.shape[0] - 1):
        for j in range(matrix.shape[1] - 1):
            submatrix = matrix[i:i + 53, j:j + 53]
            if submatrix.shape != (53, 53):
                continue
            if np.sum(submatrix) == 53 * 53 * 53:
                submatrix_count += 1
    return submatrix_count