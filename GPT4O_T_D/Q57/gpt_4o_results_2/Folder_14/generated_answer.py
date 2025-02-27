import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    target_sum = -93
    submatrices = []

    def get_submatrix_sum(r1, c1, r2, c2):
        return np.sum(matrix[r1:r2, c1:c2])
    for r1 in range(rows):
        for r2 in range(r1 + 1, rows + 1):
            for c1 in range(cols):
                for c2 in range(c1 + 1, cols + 1):
                    if get_submatrix_sum(r1, c1, r2, c2) == target_sum:
                        submatrices.append(matrix[r1:r2, c1:c2].tolist())
    return submatrices