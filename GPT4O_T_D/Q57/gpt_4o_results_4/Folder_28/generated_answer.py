import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for height in range(1, rows - i + 1):
                for width in range(1, cols - j + 1):
                    submat = matrix[i:i + height, j:j + width]
                    if np.sum(submat) == 15:
                        submatrices.append(submat)
    return submatrices