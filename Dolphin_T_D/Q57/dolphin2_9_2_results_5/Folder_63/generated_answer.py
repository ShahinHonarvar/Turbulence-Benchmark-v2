import numpy as np

def submatrix_with_particular_sum(matrix):
    row, col = matrix.shape
    sub_matrices = []
    for i in range(row - 2):
        for j in range(col - 2):
            if np.sum(matrix[i:i + 3, j:j + 3]) == 64:
                sub_matrices.append(matrix[i:i + 3, j:j + 3])
    return sub_matrices