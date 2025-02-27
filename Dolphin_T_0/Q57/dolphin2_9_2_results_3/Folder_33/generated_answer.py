import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    flat_matrix = matrix.flatten()
    for i in range(len(flat_matrix)):
        for j in range(i + 1, len(flat_matrix)):
            sub_matrix = matrix[i // matrix.shape[1], :][:, j // matrix.shape[0]]
            if sub_matrix.sum() == -811:
                result.append(sub_matrix)
    return result