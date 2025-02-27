import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrices = []
    height, width = matrix.shape
    for i in range(height - 2):
        for j in range(width - 2):
            submatrix = matrix[i:i + 3, j:j + 3]
            if len(submatrix.flatten()) == 9:
                submatrices.append(submatrix.flatten())
    return len(submatrices)