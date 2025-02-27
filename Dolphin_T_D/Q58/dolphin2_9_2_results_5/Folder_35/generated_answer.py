import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray):
        return 0
    submatrix_counter = 0
    rows, cols = matrix.shape
    for r in range(0, rows - 2):
        for c in range(0, cols - 2):
            if np.all(matrix[r:r + 3, c:c + 3] == 111):
                submatrix_counter += 1
    return submatrix_counter