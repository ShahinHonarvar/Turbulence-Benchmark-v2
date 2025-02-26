import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    target_count = 180
    submatrix_count = 0
    for i in range(rows):
        for j in range(cols):
            for height in range(1, rows - i + 1):
                for width in range(1, cols - j + 1):
                    submatrix = matrix[i:i + height, j:j + width]
                    if np.prod(submatrix.shape) == target_count:
                        submatrix_count += 1
    return submatrix_count