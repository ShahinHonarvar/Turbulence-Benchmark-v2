import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    submatrix_size = 191
    count = 0
    for r in range(rows):
        for c in range(cols):
            for subrows in range(1, rows - r + 1):
                for subcols in range(1, cols - c + 1):
                    if subrows * subcols == submatrix_size:
                        if np.prod(matrix[r:r + subrows, c:c + subcols].shape) == submatrix_size:
                            count += 1
    return count