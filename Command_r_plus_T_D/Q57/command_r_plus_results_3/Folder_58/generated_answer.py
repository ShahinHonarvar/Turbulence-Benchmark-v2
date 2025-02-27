import numpy as np

def submatrix_with_particular_sum(matrix: np.ndarray) -> list[np.ndarray]:
    rows, cols = matrix.shape
    target_sum = -137
    submatrices = []
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows + 1):
                for l in range(j, cols + 1):
                    submatrix = matrix[i:k, j:l]
                    if submatrix.size and np.sum(submatrix) == target_sum:
                        submatrices.append(submatrix)
    return submatrices