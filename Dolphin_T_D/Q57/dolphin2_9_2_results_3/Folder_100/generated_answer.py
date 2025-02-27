import numpy as np

def submatrix_with_particular_sum(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2 or matrix.dtype.kind != 'i':
        return []
    num_rows, num_cols = matrix.shape
    sub_matrices = []
    for i in range(num_rows):
        for j in range(num_cols):
            for size in range(2, min(num_rows - i + 1, num_cols - j + 1) + 1):
                sub_matrix = matrix[i:i + size, j:j + size]
                if np.sum(sub_matrix) == 28:
                    sub_matrices.append(sub_matrix)
    return sub_matrices