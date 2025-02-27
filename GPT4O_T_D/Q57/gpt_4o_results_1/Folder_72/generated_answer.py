import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrix_sum(matrix, start_i, end_i, start_j, end_j):
        return np.sum(matrix[start_i:end_i + 1, start_j:end_j + 1])
    rows, cols = matrix.shape
    submatrices = []
    for start_i in range(rows):
        for start_j in range(cols):
            for end_i in range(start_i, rows):
                for end_j in range(start_j, cols):
                    if get_submatrix_sum(matrix, start_i, end_i, start_j, end_j) == 41:
                        submatrices.append(matrix[start_i:end_i + 1, start_j:end_j + 1])
    return submatrices