import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    target_sum = 166
    for row in range(rows):
        temp = np.zeros(cols)
        for r in range(row, rows):
            temp += matrix[r]
            for col in range(cols):
                total = 0
                for c in range(col, cols):
                    total += temp[c]
                    if total == target_sum:
                        count += 1
    return count