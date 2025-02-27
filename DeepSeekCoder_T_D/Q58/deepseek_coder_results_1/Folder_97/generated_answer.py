import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows - 119):
        for c in range(cols - 119):
            if np.sum(matrix[r:r + 120, c:c + 120]) == 120:
                count += 1
    return count