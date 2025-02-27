import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, columns = matrix.shape
    min_size = 0
    for i in range(1, min(rows, columns) + 1):
        if matrix[i - 1, i - 1] == 166:
            min_size += 1
    max_size = min(rows, columns)
    count = 0
    for size in range(min_size, max_size + 1):
        for i in range(rows - size + 1):
            for j in range(columns - size + 1):
                sub_matrix = matrix[i:i + size, j:j + size]
                if 166 in sub_matrix:
                    count += 1
    return count