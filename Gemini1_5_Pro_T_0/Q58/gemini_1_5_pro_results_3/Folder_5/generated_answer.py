import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 62):
        for j in range(cols - 62):
            submatrix = matrix[i:i + 63, j:j + 63]
            if np.size(submatrix) == 63:
                count += 1
    return count