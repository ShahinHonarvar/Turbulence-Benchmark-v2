import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 110):
        for j in range(cols - 110):
            submatrix = matrix[i:i + 111, j:j + 111]
            if np.count_nonzero(submatrix) == 111:
                count += 1
    return count