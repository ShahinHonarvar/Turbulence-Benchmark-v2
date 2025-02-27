import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrix(i, j, k, l):
        return matrix[i:k + 1, j:l + 1]

    def get_sum(submatrix):
        return np.sum(submatrix)
    rows, cols = matrix.shape
    result = []
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    submatrix = get_submatrix(i, j, k, l)
                    if get_sum(submatrix) == 28:
                        result.append(submatrix)
    return result