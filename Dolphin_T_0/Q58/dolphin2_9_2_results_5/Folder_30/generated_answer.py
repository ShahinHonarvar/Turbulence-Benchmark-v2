import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows - 2):
        for j in range(cols - 2):
            if np.count_nonzero(matrix[i:i + 3, j:j + 3]) == 94:
                count += 1
    return count