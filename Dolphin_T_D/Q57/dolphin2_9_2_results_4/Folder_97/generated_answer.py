import numpy as np

def submatrix_with_particular_sum(matrix):
    matrix = np.array(matrix)
    rows, cols = matrix.shape
    submatrices = []
    for i in range(rows):
        for j in range(cols):
            for i2 in range(i + 1, rows + 1):
                for j2 in range(j + 1, cols + 1):
                    sub = np.sum(matrix[i:i2, j:j2])
                    if sub == -617:
                        submatrices.append(matrix[i:i2, j:j2])
    return submatrices