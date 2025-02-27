import numpy as np

def submatrix_with_n_numbers(matrix):
    n_elements = 43
    height = matrix.shape[0]
    width = matrix.shape[1]
    count = 0
    for i in range(height - n_elements + 1):
        for j in range(width - n_elements + 1):
            submatrix = matrix[i:i + n_elements, j:j + n_elements]
            if submatrix.size == n_elements:
                count += 1
    return count