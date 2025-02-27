import numpy as np

def submatrix_with_particular_sum(matrix: np.ndarray) -> list[np.ndarray]:
    rows, cols = matrix.shape
    submatrices = []
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == 1:
                submatrices.append(matrix[i:i + 1, j:j + 1])
    return submatrices