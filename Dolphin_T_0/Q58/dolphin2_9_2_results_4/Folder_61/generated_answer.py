import numpy as np

def submatrix_with_n_numbers(matrix):
    height = matrix.shape[0]
    width = matrix.shape[1]
    count = 0
    for h in range(height - 3):
        for w in range(width - 3):
            if len(np.unique(matrix[h:h + 4, w:w + 4])) == 4:
                count += 1
    return count