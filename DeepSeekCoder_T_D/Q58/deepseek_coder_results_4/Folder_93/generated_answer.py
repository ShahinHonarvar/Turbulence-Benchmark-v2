import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows - 1):
        for c in range(cols - 1):
            submatrix = matrix[r:r + 2, c:c + 2]
            if np.sum(submatrix) == 53:
                count += 1
    return count