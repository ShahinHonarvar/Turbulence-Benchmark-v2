import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for size in range(2, min(rows - i + 1, cols - j + 1) + 1):
                if np.sum(matrix[i:i + size, j:j + size]) == 394:
                    submatrices.append(matrix[i:i + size, j:j + size])
    return submatrices