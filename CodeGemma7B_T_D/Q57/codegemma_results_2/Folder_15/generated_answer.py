import numpy as np

def submatrix_with_particular_sum(matrix):
    result_matrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix) - i):
            for k in range(len(matrix[0])):
                for l in range(len(matrix[0]) - k):
                    submatrix = matrix[i:i + j + 1, k:k + l + 1]
                    if np.sum(submatrix) == -9:
                        result_matrices.append(submatrix)
    return result_matrices