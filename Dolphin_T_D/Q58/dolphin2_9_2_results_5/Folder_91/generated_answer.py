import numpy as np

def submatrix_with_n_numbers(matrix):
    n_submatrices = 0
    size_x, size_y = matrix.shape
    for i in range(0, size_x - 4):
        for j in range(0, size_y - 4):
            sub_matrix = matrix[i:i + 5, j:j + 5]
            if np.count_nonzero(sub_matrix == 5) == 5:
                n_submatrices += 1
    return n_submatrices