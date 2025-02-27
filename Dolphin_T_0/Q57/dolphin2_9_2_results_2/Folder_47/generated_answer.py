import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            for i in range(0, rows - r + 1):
                for j in range(0, cols - c + 1):
                    sub_matrix = matrix[i:i + r, j:j + c]
                    if np.sum(sub_matrix) == 27:
                        submatrices.append(sub_matrix)
    return submatrices