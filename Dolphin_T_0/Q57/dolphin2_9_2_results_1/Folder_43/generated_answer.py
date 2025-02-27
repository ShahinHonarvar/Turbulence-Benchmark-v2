import numpy as np

def submatrix_with_particular_sum(matrix):
    sub_matrices = []
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    for top in range(rows):
        for bottom in range(top, rows):
            for left in range(cols):
                for right in range(left, cols):
                    current_sum = np.sum(matrix[top:bottom + 1, left:right + 1])
                    if current_sum == -81:
                        sub_matrices.append(matrix[top:bottom + 1, left:right + 1])
    return sub_matrices