import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrix_sum(i, j, k, l):
        return np.sum(matrix[i:k, j:l])
    result = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for k in range(i + 1, rows + 1):
                for last_col in range(j + 1, cols + 1):
                    for first_col in range(j, last_col):
                        submatrix_sum = get_submatrix_sum(i, first_col, k, last_col)
                        if submatrix_sum == 78:
                            result.append(matrix[i:k, first_col:last_col])
    return result