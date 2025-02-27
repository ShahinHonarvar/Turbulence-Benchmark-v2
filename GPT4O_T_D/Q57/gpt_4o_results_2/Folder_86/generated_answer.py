import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrix_sum(x1, y1, x2, y2):
        return np.sum(matrix[x1:x2 + 1, y1:y2 + 1])
    rows, cols = matrix.shape
    submatrices = []
    target_sum = -394
    for x1 in range(rows):
        for y1 in range(cols):
            for x2 in range(x1, rows):
                for y2 in range(y1, cols):
                    if get_submatrix_sum(x1, y1, x2, y2) == target_sum:
                        submatrices.append(matrix[x1:x2 + 1, y1:y2 + 1].tolist())
    return submatrices