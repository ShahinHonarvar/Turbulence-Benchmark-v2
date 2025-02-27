import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(top_left, bottom_right):
        return np.sum(matrix[top_left[0]:bottom_right[0] + 1, top_left[1]:bottom_right[1] + 1])
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i, matrix.shape[0]):
                for end_col in range(j, matrix.shape[1]):
                    if submatrix_sum((i, j), (k, end_col)) == -185:
                        submatrices.append(matrix[i:k + 1, j:end_col + 1])
    return submatrices