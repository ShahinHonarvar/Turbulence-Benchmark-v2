import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    for r in range(rows):
        for c in range(cols):
            for r1 in range(r, rows):
                for c1 in range(c, cols):
                    submatrix = matrix[r:r1 + 1, c:c1 + 1]
                    if np.sum(submatrix) == 95:
                        result.append(submatrix)
    return result