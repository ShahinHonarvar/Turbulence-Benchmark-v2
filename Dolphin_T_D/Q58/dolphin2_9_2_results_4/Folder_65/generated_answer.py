import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == 35:
                sub_matrix = matrix[max(0, i - 4):min(rows, i + 5), max(0, j - 4):min(cols, j + 5)]
                if np.count_nonzero(sub_matrix == 35) == 35:
                    count += 1
    return count