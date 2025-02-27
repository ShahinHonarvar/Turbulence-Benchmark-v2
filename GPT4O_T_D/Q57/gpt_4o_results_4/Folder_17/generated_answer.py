import numpy as np

def submatrix_with_particular_sum(matrix):
    results = []
    rows, cols = matrix.shape
    for r in range(rows):
        for c in range(cols):
            for end_r in range(r, rows):
                for end_c in range(c, cols):
                    submatrix = matrix[r:end_r + 1, c:end_c + 1]
                    if np.sum(submatrix) == 398:
                        results.append(submatrix.tolist())
    return results