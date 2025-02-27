import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    target_sum = -38

    def compute_submatrix_sum(r1, c1, r2, c2):
        return matrix[r1:r2 + 1, c1:c2 + 1].sum()
    for r1 in range(rows):
        for c1 in range(cols):
            for r2 in range(r1, rows):
                for c2 in range(c1, cols):
                    if compute_submatrix_sum(r1, c1, r2, c2) == target_sum:
                        submatrices.append(matrix[r1:r2 + 1, c1:c2 + 1])
    return submatrices