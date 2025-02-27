import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for i, j in zip(range(rows - 2), range(cols - 2)):
        for k in range(i + 1, rows - 1):
            for l in range(j + 1, cols - 1):
                sub = matrix[i:k + 1, j:l + 1]
                if np.sum(sub) == 13:
                    result.append(sub.tolist())
    return result