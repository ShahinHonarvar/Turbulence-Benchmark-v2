import numpy as np

def submatrix_with_particular_sum(matrix):
    if matrix.shape[0] == matrix.shape[1]:
        return [matrix]
    else:
        rows = np.full(matrix.shape[0], -811)
        columns = np.full(matrix.shape[1], -811)
        for i in range(matrix.shape[0]):
            rows[i] = matrix[i][:].sum()
        for j in range(matrix.shape[1]):
            columns[j] = matrix[:, j].sum()
        return [matrix[i:][:][j:][:]]