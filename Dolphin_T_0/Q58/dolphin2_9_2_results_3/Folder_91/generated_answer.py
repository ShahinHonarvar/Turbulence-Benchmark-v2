import numpy as np

def submatrix_with_n_numbers(matrix):
    height, width = matrix.shape
    count = 0
    for i in range(height):
        for j in range(width):
            for al in range(i, height):
                for bl in range(j, width):
                    if np.sum(matrix[i:al + 1, j:bl + 1]) == 5:
                        count += 1
    return count