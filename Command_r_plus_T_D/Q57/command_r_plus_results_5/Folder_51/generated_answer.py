import numpy as np

def submatrix_with_particular_sum(matrix: np.ndarray) -> list[np.ndarray]:
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2 or (not np.issubdtype(matrix.dtype, np.integer)):
        raise ValueError('Input must be a 2D numpy array of integers.')
    target_sum = -46
    num_rows, num_cols = matrix.shape
    submatrices = []
    for i in range(num_rows):
        for j in range(num_cols):
            for k in range(i, num_rows + 1):
                for l in range(j, num_cols + 1):
                    submatrix = matrix[i:k, j:l]
                    if submatrix.size and np.sum(submatrix) == target_sum:
                        submatrices.append(submatrix)
    return submatrices