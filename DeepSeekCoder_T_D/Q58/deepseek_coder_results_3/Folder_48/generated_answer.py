import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows - 129):
        for c in range(cols - 129):
            if np.sum(matrix[r:r + 130, c:c + 130]) == 130:
                count += 1
    return count