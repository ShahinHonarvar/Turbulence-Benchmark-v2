import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 37):
        for j in range(cols - 37):
            submatrix = matrix[i:i + 38, j:j + 38]
            if np.size(submatrix) == 38 * 38:
                count += 1
    return count