import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows - 38):
        for c in range(cols - 38):
            if np.sum(matrix[r:r + 39, c:c + 39]) == 39:
                count += 1
    return count