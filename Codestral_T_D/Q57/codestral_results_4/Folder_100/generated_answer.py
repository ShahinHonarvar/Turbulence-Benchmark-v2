import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for left in range(cols):
        for right in range(left, cols):
            for top in range(rows):
                for bottom in range(top, rows):
                    submatrix = matrix[top:bottom + 1, left:right + 1]
                    if np.sum(submatrix) == 28:
                        submatrices.append(submatrix)
    return submatrices