import numpy as np

def submatrix_with_n_numbers(my_matrix):
    count = 0
    for r in range(len(my_matrix)):
        for c in range(len(my_matrix[0])):
            for r2 in range(r, len(my_matrix)):
                for c2 in range(c, len(my_matrix[0])):
                    sub_matrix_array = my_matrix[r:r2 + 1, c:c2 + 1]
                    if sub_matrix_array.size == 24:
                        count += 1
    return count