import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows - 9 + 1):
        for j in range(cols - 9 + 1):
            if np.size(matrix[i:i + 9, j:j + 9]) == 90:
                count += 1
    return count