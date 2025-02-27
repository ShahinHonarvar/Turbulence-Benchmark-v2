import numpy as np

def submatrix_with_particular_sum(matrix: np.ndarray) -> list[np.ndarray]:
    rows, cols = matrix.shape
    submatrices = []
    for i in range(rows):
        for j in range(cols):
            for k in range(i + 1, rows + 1):
                for l in range(j + 1, cols + 1):
                    submat = matrix[i:k, j:l]
                    if submat.size != 0 and np.sum(submat) == 38:
                        submatrices.append(submat)
    return submatrices