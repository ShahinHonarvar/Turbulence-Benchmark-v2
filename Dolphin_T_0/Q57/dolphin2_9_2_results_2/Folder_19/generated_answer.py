import numpy as np

def submatrix_with_particular_sum(matrix):
    num_rows, num_cols = matrix.shape
    sub_matrices = []
    for i in range(num_rows):
        for j in range(num_cols):
            for k in range(num_rows - i + 1):
                for l in range(num_cols - j + 1):
                    sub_matrix = matrix[i:i + k, j:j + l]
                    if np.sum(sub_matrix) == -97:
                        sub_matrices.append(sub_matrix)
    return sub_matrices