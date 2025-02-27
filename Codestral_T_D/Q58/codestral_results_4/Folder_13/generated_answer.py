import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    rows, cols = matrix.shape
    submatrix_size = int(np.sqrt(175))
    for i in range(rows - submatrix_size + 1):
        for j in range(cols - submatrix_size + 1):
            submatrix = matrix[i:i + submatrix_size, j:j + submatrix_size]
            if np.sum(submatrix) == 175:
                submatrix_count += 1
    return submatrix_count