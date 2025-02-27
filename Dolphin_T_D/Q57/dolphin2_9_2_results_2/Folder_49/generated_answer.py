import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    height, width = matrix.shape
    for i in range(height):
        for j in range(width):
            for h in range(i + 1, height + 1):
                for w in range(j + 1, width + 1):
                    sub_matrix = matrix[i:h, j:w]
                    if np.sum(sub_matrix) == -42:
                        submatrices.append(sub_matrix)
    return submatrices