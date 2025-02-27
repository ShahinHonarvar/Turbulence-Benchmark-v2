import numpy as np

def submatrix_with_particular_sum(matrix):

    def sum_submatrix(i1, j1, i2, j2):
        return np.sum(matrix[i1:i2 + 1, j1:j2 + 1])
    rows, cols = matrix.shape
    result = []
    for i1 in range(rows):
        for i2 in range(i1, rows):
            for j1 in range(cols):
                for j2 in range(j1, cols):
                    if sum_submatrix(i1, j1, i2, j2) == -10:
                        submatrix = matrix[i1:i2 + 1, j1:j2 + 1].tolist()
                        result.append(submatrix)
    return result