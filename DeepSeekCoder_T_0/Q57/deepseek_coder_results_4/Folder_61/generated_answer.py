import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for r in range(rows):
        for c in range(cols):
            for i in range(r + 1, rows + 1):
                for j in range(c + 1, cols + 1):
                    submatrix = matrix[r:i, c:j]
                    if np.sum(submatrix) == 8:
                        result.append(submatrix)
    return result