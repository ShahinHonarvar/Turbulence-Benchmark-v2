import numpy as np

def submatrix_with_n_numbers(matrix, n=54):
    x, y = matrix.shape
    x_l = y_l = n
    result_counter = 0
    for i in range(x - x_l + 1):
        for j in range(y - y_l + 1):
            result_submatrix = matrix[i:x_l + i, j:y_l + j]
            if len(result_submatrix) == n:
                result_counter += 1
    if result_counter > 0:
        return result_counter
    else:
        return 0