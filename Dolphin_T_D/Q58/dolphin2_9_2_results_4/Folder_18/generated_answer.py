import numpy as np

def submatrix_with_n_numbers(matrix):
    height = len(matrix)
    width = len(matrix[0])
    count = 0
    for i in range(height - 3):
        for j in range(width - 3):
            if np.all(matrix[i:i + 4, j:j + 4] == 104):
                count += 1
    return count