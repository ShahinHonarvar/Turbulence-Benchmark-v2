import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for r in range(rows):
        for c in range(cols):
            for h in range(1, rows - r + 1):
                for w in range(1, cols - c + 1):
                    submatrix = matrix[r:r + h, c:c + w]
                    if np.sum(submatrix) == 8:
                        result.append(submatrix)
    return result