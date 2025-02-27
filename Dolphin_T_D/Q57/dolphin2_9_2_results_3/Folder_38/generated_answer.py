import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for i2 in range(i + 1, rows + 1):
                for j2 in range(j + 1, cols + 1):
                    submatrix = matrix[i:i2, j:j2]
                    if np.sum(submatrix) == 34:
                        result.append(submatrix)
    return result