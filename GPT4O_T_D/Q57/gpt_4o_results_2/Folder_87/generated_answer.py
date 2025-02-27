import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(x1, y1, x2, y2):
        submatrix = matrix[x1:x2 + 1, y1:y2 + 1]
        return np.sum(submatrix)
    num_rows, num_cols = matrix.shape
    result = []
    for x1 in range(num_rows):
        for y1 in range(num_cols):
            for x2 in range(x1, num_rows):
                for y2 in range(y1, num_cols):
                    if submatrix_sum(x1, y1, x2, y2) == 35:
                        result.append(matrix[x1:x2 + 1, y1:y2 + 1].tolist())
    return result