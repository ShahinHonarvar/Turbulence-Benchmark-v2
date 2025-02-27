import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    total_length = len(matrix) * len(matrix[0])
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if total_length - (len(matrix) - i) * (len(matrix[0]) - j) < 24:
                break
            submatrix = matrix[i:i + 2, j:j + 12]
            if submatrix.shape[0] * submatrix.shape[1] == 24:
                count += 1
    return count