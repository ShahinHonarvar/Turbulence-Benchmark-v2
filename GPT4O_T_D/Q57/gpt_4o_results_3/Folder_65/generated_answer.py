import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    sub_matrices = []
    for start_i in range(rows):
        for start_j in range(cols):
            for end_i in range(start_i + 1, rows + 1):
                for end_j in range(start_j + 1, cols + 1):
                    submatrix = matrix[start_i:end_i, start_j:end_j]
                    if np.sum(submatrix) == 78:
                        sub_matrices.append(submatrix.tolist())
    return sub_matrices