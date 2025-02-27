import numpy as np

def submatrix_with_n_numbers(matrix):
    num_elements = 120
    submatrix_count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i + num_elements <= len(matrix) and j + num_elements <= len(matrix[0]):
                if np.all(matrix[i:i + num_elements, j:j + num_elements]):
                    submatrix_count += 1
    return submatrix_count