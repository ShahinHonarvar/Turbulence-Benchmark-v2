import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    if not isinstance(matrix, np.ndarray):
        raise ValueError('Input must be a numpy ndarray.')
    rows, cols = matrix.shape
    target_sum = 77
    count = 0
    for i in range(rows):
        for j in range(cols):
            if i + 3 < rows and j + 3 < cols:
                submatrix = matrix[i:i + 3, j:j + 3]
                if np.sum(submatrix) == target_sum:
                    count += 1
    return count