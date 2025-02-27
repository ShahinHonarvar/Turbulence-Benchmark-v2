import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, columns = matrix.shape
    for i in range(rows):
        for j in range(columns):
            if matrix[i, j] == 51:
                for size in range(2, min(rows - i, columns - j) + 1):
                    if np.sum(matrix[i:i + size, j:j + size]) == 51:
                        count += 1
    return count