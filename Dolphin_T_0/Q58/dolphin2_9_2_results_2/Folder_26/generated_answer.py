import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 115
    rows, cols = matrix.shape
    count = 0
    for i in range(0, rows - n + 1):
        for j in range(0, cols - n + 1):
            sub_matrix = matrix[i:i + n, j:j + n]
            num_elements = sub_matrix.shape[0] * sub_matrix.shape[1]
            if num_elements == n:
                count += 1
    if count == 0:
        return 0
    else:
        return count