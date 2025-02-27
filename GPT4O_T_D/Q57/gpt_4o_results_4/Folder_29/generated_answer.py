import numpy as np

def submatrix_with_particular_sum(matrix):

    def calculate_sum(matrix, top, left, bottom, right):
        return np.sum(matrix[top:bottom + 1, left:right + 1])
    n_rows, n_cols = matrix.shape
    result = []
    for top in range(n_rows):
        for left in range(n_cols):
            for bottom in range(top, n_rows):
                for right in range(left, n_cols):
                    if calculate_sum(matrix, top, left, bottom, right) == 84:
                        result.append(matrix[top:bottom + 1, left:right + 1].tolist())
    return result