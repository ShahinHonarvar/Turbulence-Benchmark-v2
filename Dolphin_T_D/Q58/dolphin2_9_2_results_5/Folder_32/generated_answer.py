import numpy as np

def submatrix_with_n_numbers(matrix):
    num_elements = matrix.size
    num_to_find = 103
    counter = 0
    for sub_matrix_size in range(1, num_elements + 1):
        if num_elements % sub_matrix_size == 0:
            if num_to_find % sub_matrix_size == 0:
                counter += 1
    return counter