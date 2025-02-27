import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows - 12):
        for c in range(cols - 12):
            if np.sum(matrix[r:r + 13, c:c + 13]) == 13:
                count += 1
    return count