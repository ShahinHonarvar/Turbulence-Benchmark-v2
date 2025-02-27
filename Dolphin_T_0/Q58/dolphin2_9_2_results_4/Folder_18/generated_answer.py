import numpy as np

def submatrix_with_n_numbers(matrix):
    num_elements = 104
    result = 0
    shape = matrix.shape
    for i in range(shape[0]):
        for j in range(shape[1]):
            for n in range(i + num_elements, shape[0] + 1):
                for m in range(j + num_elements, shape[1] + 1):
                    if (n - i) * (m - j) == num_elements:
                        temp_matrix = matrix[i:n, j:m]
                        if len(temp_matrix) == num_elements:
                            result += 1
    return result