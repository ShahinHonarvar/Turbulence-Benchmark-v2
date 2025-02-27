import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 75):
        for j in range(cols - 75):
            for k in range(i + 76, rows + 1):
                for l in range(j + 76, cols + 1):
                    if np.prod(matrix[i:k, j:l].shape) == 76:
                        count += 1
    return count