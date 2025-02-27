import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    target_sum = 118
    for row in range(rows):
        temp = np.zeros(cols)
        for r in range(row, rows):
            temp += matrix[r]
            left = 0
            current_sum = 0
            for right in range(cols):
                current_sum += temp[right]
                while current_sum > target_sum and left <= right:
                    current_sum -= temp[left]
                    left += 1
                if current_sum == target_sum:
                    count += 1
    return count