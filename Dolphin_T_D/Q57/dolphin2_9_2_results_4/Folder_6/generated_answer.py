import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for i in range(rows - 1):
        for j in range(cols - 1):
            for bottom in range(i, rows):
                for right in range(j, cols):
                    if np.sum(matrix[i:bottom + 1, j:right + 1]) == 126:
                        submatrices.append(matrix[i:bottom + 1, j:right + 1])
    return submatrices