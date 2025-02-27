import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            if i + 12 <= rows and j + 12 <= cols:
                submatrix = matrix[i:i + 12, j:j + 12]
                if np.size(submatrix) == 180:
                    count += 1
    return count