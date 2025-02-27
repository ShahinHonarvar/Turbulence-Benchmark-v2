import numpy as np

def submatrix_with_n_numbers(matrix):
    matrix = np.array(matrix)
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for size in range(min(i + 1, j + 1), min(rows - i, cols - j) + 1):
                if np.count_nonzero(matrix[i:i + size, j:j + size]) == 17:
                    count += 1
    return count