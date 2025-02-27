import numpy as np

def submatrix_with_particular_sum(matrix):
    size_x, size_y = matrix.shape
    submatrices = []
    for x in range(size_x):
        for y in range(size_y):
            for x2 in range(x, size_x):
                for y2 in range(y, size_y):
                    sub_matrix = matrix[x:x2 + 1, y:y2 + 1]
                    if np.sum(sub_matrix) == -452:
                        submatrices.append(sub_matrix)
    return submatrices