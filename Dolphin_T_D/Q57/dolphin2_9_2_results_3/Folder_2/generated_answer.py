import numpy as np

def submatrix_with_particular_sum(matrix):
    results = []
    n, m = matrix.shape
    for x1 in range(n):
        for x2 in range(x1, n):
            for y1 in range(m):
                for y2 in range(y1, m):
                    submatrix = matrix[x1:x2 + 1, y1:y2 + 1]
                    if np.sum(submatrix) == -863:
                        results.append(submatrix)
    return results