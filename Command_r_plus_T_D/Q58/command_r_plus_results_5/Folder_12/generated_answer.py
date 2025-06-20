import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 1):
        for j in range(cols - 1):
            if matrix[i][j] + matrix[i][j + 1] + matrix[i + 1][j] + matrix[i + 1][j + 1] == 46:
                count += 1
    return count