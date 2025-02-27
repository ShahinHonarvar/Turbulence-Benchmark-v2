import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            for r in range(rows - i + 1):
                for c in range(cols - j + 1):
                    submatrix = matrix[r:r + i, c:c + j]
                    if np.sum(submatrix) == 997:
                        result.append(submatrix)
    return result