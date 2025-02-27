import numpy as np

def submatrix_with_n_numbers(matrix):
    height, width = matrix.shape
    count = 0
    for i in range(height - 4):
        for j in range(width - 4):
            sub_matrix = matrix[i:i + 5, j:j + 5]
            if np.count_nonzero(sub_matrix == 49) == 5:
                count += 1
    return count