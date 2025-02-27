import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    height = len(matrix)
    width = len(matrix[0])
    for i in range(height - 10):
        for j in range(width - 10):
            if np.all(matrix[i:i + 11, j:j + 11] == 91):
                count += 1
    return count