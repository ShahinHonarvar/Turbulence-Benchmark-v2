import numpy as np

def submatrix_with_n_numbers(matrix):
    H, W = matrix.shape
    count = 0
    for h in range(H - 15):
        for w in range(W - 15):
            if (matrix[h:h + 16, w:w + 16] == 179).all():
                count += 1
    return count