import numpy as np

def submatrix_with_n_numbers(matrix):
    shape_matrix = matrix.shape
    count = 0
    for i in range(shape_matrix[0] - 11):
        for j in range(shape_matrix[1] - 11):
            sub_matrix = matrix[i:i + 12, j:j + 12]
            if np.sum(sub_matrix) == 144:
                count += 1
    return count