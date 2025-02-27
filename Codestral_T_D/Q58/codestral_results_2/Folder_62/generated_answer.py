import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    submatrix_size = 186
    elements_in_submatrix = submatrix_size * submatrix_size
    for i in range(rows - submatrix_size + 1):
        for j in range(cols - submatrix_size + 1):
            submatrix = matrix[i:i + submatrix_size, j:j + submatrix_size]
            if np.count_nonzero(submatrix) == elements_in_submatrix:
                count += 1
    return count