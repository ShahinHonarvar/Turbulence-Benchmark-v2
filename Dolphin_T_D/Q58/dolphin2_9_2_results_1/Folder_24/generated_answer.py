import numpy as np

def submatrix_with_n_numbers(matrix):
    num_elements = 51
    sub_matrix_count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for x in range(i, len(matrix)):
                for y in range(j, len(matrix[0])):
                    if len(matrix[i:x + 1, j:y + 1].flatten()) == num_elements:
                        sub_matrix_count += 1
    return sub_matrix_count if sub_matrix_count > 0 else 0