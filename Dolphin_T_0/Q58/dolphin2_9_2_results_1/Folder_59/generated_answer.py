import numpy as np

def submatrix_with_n_numbers(matrix):
    row, col = matrix.shape
    count = 0
    for r in range(row):
        for c in range(col):
            for dr in range(row - r):
                for dc in range(col - c):
                    if (dr + 1) * (dc + 1) == 76:
                        submatrix_sum = np.sum(matrix[r:r + dr + 1, c:c + dc + 1])
                        if submatrix_sum == 76:
                            count += 1
    return count