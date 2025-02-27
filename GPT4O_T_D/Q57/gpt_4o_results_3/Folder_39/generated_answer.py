import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrix_sum(matrix, i1, j1, i2, j2):
        return np.sum(matrix[i1:i2 + 1, j1:j2 + 1])
    rows, cols = matrix.shape
    results = []
    for i in range(rows):
        for j in range(cols):
            for i2 in range(i, rows):
                for j2 in range(j, cols):
                    if get_submatrix_sum(matrix, i, j, i2, j2) == 66:
                        submatrix = matrix[i:i2 + 1, j:j2 + 1].tolist()
                        results.append(submatrix)
    return results