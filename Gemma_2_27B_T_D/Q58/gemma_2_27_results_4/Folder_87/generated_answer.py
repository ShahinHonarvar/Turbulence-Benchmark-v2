import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 9 + 1):
        for j in range(matrix.shape[1] - 9 + 1):
            submatrix = matrix[i:i + 9, j:j + 9]
            if submatrix.size == 96:
                count += 1
    return count