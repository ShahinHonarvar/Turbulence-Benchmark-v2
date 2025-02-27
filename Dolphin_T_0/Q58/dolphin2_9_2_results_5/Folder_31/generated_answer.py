import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if i - 3 >= 0 and j - 3 >= 0:
                sub_matrix = matrix[i - 3:i + 1, j - 3:j + 1]
                if np.count_nonzero(sub_matrix) == 45:
                    count += 1
    return count