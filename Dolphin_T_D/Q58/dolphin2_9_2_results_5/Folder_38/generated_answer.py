import numpy as np

def submatrix_with_n_numbers(matrix):
    h, w = matrix.shape
    count = 0
    for i in range(h - 2):
        for j in range(w - 2):
            sub_matrix = matrix[i:i + 3, j:j + 3]
            if np.count_nonzero(sub_matrix) == 34:
                count += 1
    return count