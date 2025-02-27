import numpy as np

def submatrix_with_particular_sum(matrix: np.ndarray) -> list:
    h, w = matrix.shape
    submatrices = []
    for r1 in range(h):
        for c1 in range(w):
            for r2 in range(r1 + 1, h + 1):
                for c2 in range(c1 + 1, w + 1):
                    if np.sum(matrix[r1:r2, c1:c2]) == -255:
                        submatrices.append(matrix[r1:r2, c1:c2])
    return submatrices