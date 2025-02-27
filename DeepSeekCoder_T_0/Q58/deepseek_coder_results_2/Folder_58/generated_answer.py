import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows - 184):
        for c in range(cols - 184):
            if np.sum(matrix[r:r + 185, c:c + 185]) == 185:
                count += 1
    return count