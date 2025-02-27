import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 76):
        for j in range(cols - 76):
            submatrix = matrix[i:i + 77, j:j + 77]
            if np.size(submatrix) == 77 * 77:
                count += 1
    return count