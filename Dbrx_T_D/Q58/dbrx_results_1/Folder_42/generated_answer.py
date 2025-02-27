import numpy as np

def submatrix_with_n_numbers(matrix):
    n_rows, n_cols = matrix.shape
    count = 0
    for i in range(n_rows - 1, -1, -1):
        for j in range(n_cols - 1, -1, -1):
            current_sum = 0
            for k in range(i, n_rows):
                for l in range(j, n_cols):
                    current_sum += matrix[k, l]
                    if current_sum == 193:
                        count += 1
                        break
                if current_sum >= 193:
                    break
    return count