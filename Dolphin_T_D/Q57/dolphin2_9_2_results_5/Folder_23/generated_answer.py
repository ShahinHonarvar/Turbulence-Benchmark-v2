import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for x in range(i + 1, rows + 1):
                for y in range(j + 1, cols + 1):
                    submatrix_sum = np.sum(matrix[i:x, j:y])
                    if submatrix_sum == 59:
                        submatrices.append(matrix[i:x, j:y])
    return submatrices