import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    sub_matrices = []
    for size in range(1, min(rows, cols) + 1):
        for i in range(rows - size + 1):
            for j in range(cols - size + 1):
                sub_matrix = matrix[i:i + size, j:j + size]
                if np.sum(sub_matrix) == -261:
                    sub_matrices.append(sub_matrix)
    return sub_matrices