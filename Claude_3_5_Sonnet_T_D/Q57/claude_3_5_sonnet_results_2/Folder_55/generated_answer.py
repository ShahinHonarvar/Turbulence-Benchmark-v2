import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for h in range(i, rows):
                for w in range(j, cols):
                    submatrix = matrix[i:h + 1, j:w + 1]
                    if np.sum(submatrix) == 1:
                        result.append(submatrix.tolist())
    return result