import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for row in range(rows - 5):
        for col in range(cols - 5):
            submatrix = matrix[row:row + 6, col:col + 6]
            if submatrix.size == 39 and np.unique(submatrix).size == 39:
                count += 1
    return count