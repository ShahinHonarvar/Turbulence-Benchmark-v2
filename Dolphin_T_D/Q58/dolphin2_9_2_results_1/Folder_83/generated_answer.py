import numpy as np

def submatrix_with_n_numbers(matrix):
    h, w = matrix.shape
    count = 0
    for i in range(h):
        for j in range(w):
            if matrix[i, j] == 47:
                if i > 0 and j > 0 and (matrix[i - 1, j - 1] == 47) and (matrix[i - 1, j] == 47) and (matrix[i, j - 1] == 47):
                    count += 1
    return count