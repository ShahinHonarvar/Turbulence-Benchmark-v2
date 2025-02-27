import numpy as np

def submatrix_with_n_numbers(matrix):
    num_of_submatrices = 0
    matrix_height = matrix.shape[0]
    matrix_width = matrix.shape[1]
    for i in range(matrix_height):
        for j in range(matrix_width):
            for height_range in range(i + 1, matrix_height + 1):
                for width_range in range(j + 1, matrix_width + 1):
                    if width_range - j + 1 == 130 and height_range - i + 1 == 130:
                        num_of_submatrices += 1
    return num_of_submatrices