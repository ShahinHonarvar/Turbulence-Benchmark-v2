import numpy as np

def submatrix_with_n_numbers(matrix):
    num_elements = 35
    rows, cols = matrix.shape
    counter = 0
    for i in range(rows - num_elements + 1):
        for j in range(cols - num_elements + 1):
            counter += np.sum(matrix[i:i + num_elements, j:j + num_elements] == num_elements)
    return counter