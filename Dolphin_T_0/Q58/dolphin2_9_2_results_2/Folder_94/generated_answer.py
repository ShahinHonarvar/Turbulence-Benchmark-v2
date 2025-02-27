import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrices = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if np.array_equal(matrix[i:i + 3, j:j + 3], [[9, 3], [3, 2], [1, 1]]):
                submatrices += 1
    return submatrices