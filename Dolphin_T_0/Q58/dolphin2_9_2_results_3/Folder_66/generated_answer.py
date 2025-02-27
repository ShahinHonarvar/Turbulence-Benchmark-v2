import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    num_elements = matrix.shape[0] * matrix.shape[1]
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i:i + 42].shape[0] == 42 and matrix[:, j:j + 42].shape[1] == 42:
                count += 1
    return count if num_elements == count * 42 else 0