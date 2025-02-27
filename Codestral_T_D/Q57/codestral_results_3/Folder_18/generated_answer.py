import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            for i in range(rows - r + 1):
                for j in range(cols - c + 1):
                    submatrix = matrix[i:i + r, j:j + c]
                    if np.sum(submatrix) == 616:
                        submatrices.append(submatrix)
    return submatrices