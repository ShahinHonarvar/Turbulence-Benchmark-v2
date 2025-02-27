import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows - 71):
        for c in range(cols - 71):
            if np.size(matrix[r:r + 72, c:c + 72]) == 72:
                count += 1
    return count