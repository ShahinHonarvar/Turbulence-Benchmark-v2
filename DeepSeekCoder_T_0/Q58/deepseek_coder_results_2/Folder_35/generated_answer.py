import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows - 2):
        for c in range(cols - 2):
            submatrix = matrix[r:r + 3, c:c + 3]
            if np.sum(submatrix) == 111:
                count += 1
    return count