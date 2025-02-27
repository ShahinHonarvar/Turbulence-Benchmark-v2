import numpy as np

def submatrix_with_n_numbers(matrix):
    numbers = 191
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - numbers + 1):
        for j in range(cols - numbers + 1):
            if np.sum(matrix[i:i + numbers, j:j + numbers]) == numbers * numbers:
                count += 1
    return count