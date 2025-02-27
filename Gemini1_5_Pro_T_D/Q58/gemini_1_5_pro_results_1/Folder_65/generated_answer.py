import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 34):
        for j in range(cols - 34):
            submatrix = matrix[i:i + 35, j:j + 35]
            if np.size(submatrix) == 35 * 35:
                count += 1
    return count