import numpy as np

def submatrix_with_n_numbers(matrix):
    matrix = np.array(matrix, dtype=int)
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            if i + 14 < rows and j + 14 < cols:
                if np.count_nonzero(matrix[i:i + 14, j:j + 14]) == 186:
                    count += 1
    return count