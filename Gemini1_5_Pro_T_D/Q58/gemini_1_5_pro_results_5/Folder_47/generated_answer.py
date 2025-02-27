import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 9 + 1):
        for j in range(cols - 9 + 1):
            submatrix = matrix[i:i + 9, j:j + 9]
            if np.size(submatrix) == 90:
                count += 1
    return count