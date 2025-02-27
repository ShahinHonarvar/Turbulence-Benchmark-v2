import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    target_sum = 411
    for top in range(rows):
        for left in range(cols):
            for bottom in range(top, rows):
                for right in range(left, cols):
                    submatrix = matrix[top:bottom + 1, left:right + 1]
                    if np.sum(submatrix) == target_sum:
                        submatrices.append(submatrix.copy())
    return submatrices