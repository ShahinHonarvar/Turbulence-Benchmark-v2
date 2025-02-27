import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    target_sum = 185
    for row in range(rows):
        temp = np.zeros(cols)
        for r in range(row, rows):
            temp += matrix[r]
            sum_ = 0
            for col in range(cols):
                sum_ += temp[col]
                if sum_ == target_sum:
                    count += 1
                elif sum_ > target_sum:
                    sum_ = 0
    return count