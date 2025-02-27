import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 9):
        for j in range(matrix.shape[1] - 9):
            submatrix = matrix[i:i + 10, j:j + 10]
            if submatrix.size == 100:
                count += 1
    return count