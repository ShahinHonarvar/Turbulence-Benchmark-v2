import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for last_col in range(j, cols):
                    submatrix = matrix[i:k + 1, j:last_col + 1]
                    if np.sum(submatrix) == 126:
                        result.append(submatrix.tolist())
    return result