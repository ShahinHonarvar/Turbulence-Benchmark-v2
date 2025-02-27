import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            if i + 5 < rows and j + 3 < cols:
                if np.sum(matrix[i:i + 5, j:j + 3]) == 39 * 15:
                    count += 1
    return count