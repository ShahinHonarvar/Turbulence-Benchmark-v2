import numpy as np

def submatrix_with_particular_sum(matrix):

    def sum_submatrix(x1, y1, x2, y2):
        submatrix = matrix[x1:x2 + 1, y1:y2 + 1]
        return np.sum(submatrix)
    rows, cols = matrix.shape
    result = []
    for x1 in range(rows):
        for y1 in range(cols):
            for x2 in range(x1, rows):
                for y2 in range(y1, cols):
                    if sum_submatrix(x1, y1, x2, y2) == 66:
                        result.append(matrix[x1:x2 + 1, y1:y2 + 1].tolist())
    return result