import numpy as np

def submatrix_with_n_numbers(matrix):
    shape = matrix.shape
    num_rows = shape[0]
    num_cols = shape[1]
    counter = 0
    for n in range(120, num_rows * num_cols, 120):
        for i in range(num_rows - n + 1):
            for j in range(num_cols - n + 1):
                submatrix = matrix[i:i + n, j:j + n]
                if len(submatrix) == 120 and sum(submatrix.flatten()) == n:
                    counter += 1
    return counter