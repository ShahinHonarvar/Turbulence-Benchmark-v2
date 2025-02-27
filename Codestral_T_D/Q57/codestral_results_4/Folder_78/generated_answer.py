import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for r in range(rows):
        for c in range(cols):
            for r_size in range(1, rows - r + 1):
                for c_size in range(1, cols - c + 1):
                    submatrix = matrix[r:r + r_size, c:c + c_size]
                    if submatrix.sum() == 17:
                        submatrices.append(submatrix)
    return submatrices