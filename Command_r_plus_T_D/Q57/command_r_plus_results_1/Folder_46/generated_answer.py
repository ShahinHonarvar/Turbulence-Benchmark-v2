import numpy as np

def submatrix_with_particular_sum(matrix: np.ndarray) -> list[np.ndarray]:
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        raise ValueError('Input must be a 2D numpy array.')
    rows, cols = matrix.shape
    target_sum = 416
    submatrices = []
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows + 1):
                for l in range(j, cols + 1):
                    sub_matrix = matrix[i:k, j:l]
                    if sub_matrix.size and np.sum(sub_matrix) == target_sum:
                        submatrices.append(sub_matrix)
    return submatrices