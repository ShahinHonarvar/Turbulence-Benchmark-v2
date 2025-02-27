import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows - 79):
        for c in range(cols - 79):
            if np.size(matrix[r:r + 80, c:c + 80]) == 6400:
                count += 1
    return count