import numpy as np

def submatrix_with_particular_sum(matrix: np.ndarray) -> list[np.ndarray]:
    rows, cols = matrix.shape
    submatrices = []
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            for row_start in range(rows - i + 1):
                for col_start in range(cols - j + 1):
                    submatrix = matrix[row_start:row_start + i, col_start:col_start + j]
                    if np.sum(submatrix) == 15:
                        submatrices.append(submatrix)
    return submatrices