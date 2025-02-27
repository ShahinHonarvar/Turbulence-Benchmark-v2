import numpy as np

def submatrix_with_n_numbers(matrix):
    num_rows, num_cols = matrix.shape
    max_possible_size = min(num_rows, num_cols)
    count = 0
    for size in range(1, max_possible_size + 1):
        if size * size != 103:
            continue
        for i in range(num_rows - size + 1):
            for j in range(num_cols - size + 1):
                submatrix = matrix[i:i + size, j:j + size]
                if submatrix.size == 103:
                    count += 1
    return count