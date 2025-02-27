import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 9):
        for j in range(cols - 9):
            submatrix = matrix[i:i + 10, j:j + 10]
            if np.size(submatrix) == 96:
                count += 1
    return count