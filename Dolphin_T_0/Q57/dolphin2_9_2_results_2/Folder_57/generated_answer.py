import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for i in range(rows):
        for j in range(cols):
            for size_i in range(i + 1, rows + 1):
                for size_j in range(j + 1, cols + 1):
                    submat = matrix[i:size_i, j:size_j]
                    if np.sum(submat) == 13:
                        submatrices.append(submat)
    return submatrices