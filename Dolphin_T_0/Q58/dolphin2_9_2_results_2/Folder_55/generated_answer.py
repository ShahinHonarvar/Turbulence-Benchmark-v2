import numpy as np

def submatrix_with_n_numbers(matrix):
    flat_matrix = matrix.flatten()
    submatrixes = []
    for i in range(len(flat_matrix) - 38):
        submatrixes.append(flat_matrix[i:i + 39])
    count = 0
    for submatrix in submatrixes:
        if len(submatrix) == 39:
            count += 1
    return count if count != 0 else 0