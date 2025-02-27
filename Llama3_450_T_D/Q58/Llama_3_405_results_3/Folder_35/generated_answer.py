import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    target_sum = 111
    for r in range(rows):
        temp = np.zeros(cols)
        for c in range(r, rows):
            temp += matrix[c]
            left = 0
            current_sum = 0
            for right in range(cols):
                current_sum += temp[right]
                while current_sum > target_sum:
                    current_sum -= temp[left]
                    left += 1
                if current_sum == target_sum:
                    count += 1
    return count