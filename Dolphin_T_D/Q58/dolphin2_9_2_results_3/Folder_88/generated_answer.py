import numpy as np

def submatrix_with_n_numbers(matrix):
    height, width = matrix.shape
    count = 0
    for i in range(height):
        for j in range(width):
            for h in range(i, height):
                for w in range(j, width):
                    if np.count_nonzero(matrix[i:h + 1, j:w + 1]) == 67:
                        count += 1
    return count