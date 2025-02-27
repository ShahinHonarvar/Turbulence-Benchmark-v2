import numpy as np

def submatrix_with_particular_sum(matrix):
    h, w = matrix.shape
    submatrices = []
    for y in range(h):
        for x in range(w):
            for size_y in range(1, h - y + 1):
                for size_x in range(1, w - x + 1):
                    sub_matrix = matrix[y:y + size_y, x:x + size_x]
                    if np.sum(sub_matrix) == 616:
                        submatrices.append(sub_matrix.tolist())
    return submatrices