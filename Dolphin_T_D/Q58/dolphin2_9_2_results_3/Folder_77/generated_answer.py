import numpy as np

def submatrix_with_n_numbers(matrix):
    num_elements = 179
    count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i:i + num_elements, j:j + num_elements].size == num_elements ** 2:
                count += 1
    return count