import numpy as np

def submatrix_with_particular_sum(matrix: np.ndarray) -> list[np.ndarray]:
    rows, cols = matrix.shape
    result = []
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows + 1):
                for l in range(j, cols + 1):
                    submatrix = matrix[i:k, j:l]
                    if submatrix.size and np.sum(submatrix) == 616:
                        result.append(submatrix)
    return result