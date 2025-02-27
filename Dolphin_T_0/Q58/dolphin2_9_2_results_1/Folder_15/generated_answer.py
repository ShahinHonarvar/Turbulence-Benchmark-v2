import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows - 1):
        for j in range(cols - 1):
            if len(np.unique(matrix[i:i + 2, j:j + 2])) == 2:
                count += 1
    return count