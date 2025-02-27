import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 146):
        for j in range(cols - 146):
            submatrix = matrix[i:i + 147, j:j + 147]
            if np.size(submatrix) == 147:
                count += 1
    return count