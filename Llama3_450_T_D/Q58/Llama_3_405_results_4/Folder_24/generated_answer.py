import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    target_sum = 51
    for r in range(rows):
        for c in range(cols):
            sum_matrix = np.zeros((rows, cols))
            sum_matrix[r, c] = matrix[r, c]
            for i in range(r, rows):
                for j in range(c, cols):
                    if i > r:
                        sum_matrix[i, j] = sum_matrix[i - 1, j] + matrix[i, j]
                    if j > c:
                        sum_matrix[i, j] = sum_matrix[i, j - 1] + matrix[i, j]
                    if i > r and j > c:
                        sum_matrix[i, j] = sum_matrix[i - 1, j - 1] + sum_matrix[i - 1, j] + sum_matrix[i, j - 1] - sum_matrix[i - 1, j - 1] + matrix[i, j]
                    if sum_matrix[i, j] == target_sum:
                        count += 1
    return count