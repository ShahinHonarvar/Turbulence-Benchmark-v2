import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    total_elements = rows * cols
    n_numbers = 126
    if total_elements == 0 or total_elements < n_numbers:
        return 0
    count = 0
    for i in range(rows - n_numbers + 1):
        for j in range(cols - n_numbers + 1):
            if (matrix[i:i + n_numbers, j:j + n_numbers] == 126).all():
                count += 1
    return count