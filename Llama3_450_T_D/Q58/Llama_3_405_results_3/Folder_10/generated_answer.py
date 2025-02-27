import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    target_sum = 56
    for row in range(rows):
        for col in range(cols):
            current_sum = 0
            for i in range(row, rows):
                current_sum += np.sum(matrix[i, col:])
                if current_sum == target_sum:
                    count += 1
            current_sum = 0
            for j in range(col, cols):
                current_sum += np.sum(matrix[row:, j])
                if current_sum == target_sum:
                    count += 1
    return count // 2