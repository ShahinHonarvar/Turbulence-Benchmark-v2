import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    for r in range(rows):
        for c in range(cols):
            for size in range(2, min(rows - r + 1, cols - c + 1) + 1):
                submatrix = matrix[r:r + size, c:c + size]
                if np.sum(submatrix) == 28:
                    submatrices.append(submatrix)
    return submatrices