import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    count = 0
    for i in range(rows):
        for j in range(cols):
            if i + 9 >= rows or j + 9 >= cols:
                continue
            submatrix = matrix[i:i + 10, j:j + 10]
            if np.size(submatrix) == 96:
                count += 1
    return count