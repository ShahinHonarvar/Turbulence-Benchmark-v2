import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for i in range(rows):
        for j in range(cols):
            for h in range(rows - i + 1):
                for w in range(cols - j + 1):
                    submatrix_sum = np.sum(matrix[i:i + h, j:j + w])
                    if submatrix_sum == -10:
                        submatrices.append(matrix[i:i + h, j:j + w])
    return submatrices