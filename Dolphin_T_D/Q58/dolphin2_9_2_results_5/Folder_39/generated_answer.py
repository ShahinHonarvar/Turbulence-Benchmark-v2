import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    size_matrix = len(matrix)
    for i in range(size_matrix):
        for j in range(i + 1, size_matrix):
            submatrix = matrix[i:j + 1, :]
            if np.size(submatrix) == 59:
                submatrix_count += 1
    return submatrix_count