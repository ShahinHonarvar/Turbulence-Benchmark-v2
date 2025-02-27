import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for size_i in range(i + 1, rows + 1):
                for size_j in range(j + 1, cols + 1):
                    if np.sum(matrix[i:size_i, j:size_j]) == 416:
                        submatrices.append(matrix[i:size_i, j:size_j])
    return submatrices