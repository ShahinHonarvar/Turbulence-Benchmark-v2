import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    shape = matrix.shape
    for i in range(shape[0] - 82):
        for j in range(shape[1] - 82):
            submatrix = matrix[i:i + 83, j:j + 83]
            if submatrix.size == 83 * 83:
                count += 1
    return count