import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for i in range(rows):
        for j in range(cols):
            for size in range(2, min(rows - i + 1, cols - j + 1) + 1):
                submatrix_sum = np.sum(matrix[i:i + size, j:j + size])
                if submatrix_sum == 8:
                    submatrices.append(matrix[i:i + size, j:j + size])
    return submatrices