import numpy as np

def submatrix_with_particular_sum(matrix):

    def calculate_submatrix_sum(x1, y1, x2, y2):
        return np.sum(matrix[x1:x2 + 1, y1:y2 + 1])
    num_rows, num_cols = matrix.shape
    submatrices = []
    for x1 in range(num_rows):
        for y1 in range(num_cols):
            for x2 in range(x1, num_rows):
                for y2 in range(y1, num_cols):
                    if calculate_submatrix_sum(x1, y1, x2, y2) == 901:
                        submatrices.append(matrix[x1:x2 + 1, y1:y2 + 1].tolist())
    return submatrices